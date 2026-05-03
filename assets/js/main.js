/* ═══════════════════════════════════════════════════════════════
   ULTRAMETRIC PARADIGM — Content-Driven Interactive Engine
   ═══════════════════════════════════════════════════════════════ */
(function(){
  'use strict';
  var $=function(s){return document.querySelector(s);};
  var $$=function(s){return document.querySelectorAll(s);};
  var NAV=$('#sidebar-nav'),MAIN=$('#main-content'),SIDEBAR=$('#sidebar');
  var OVERLAY=$('.sidebar-overlay'),PROGRESS=$('.progress-bar');
  var SCROLL_OFFSET=80,DEBOUNCE_MS=300;

  /* ── Theme ──────────────────────────────────────── */
  function toggleTheme(){
    var next=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
    document.documentElement.setAttribute('data-theme',next);
    localStorage.setItem('theme',next);
    $$('.theme-toggle,.theme-toggle-mobile').forEach(function(b){b.textContent=next==='dark'?'☀️':'🌙';});
  }

  /* ── Sidebar Nav Builder ────────────────────────── */
  function buildSidebar(){
    var headings=$$('#main-content h1,#main-content h2,#main-content h3');
    var frag=document.createDocumentFragment();
    var tocs=[];
    headings.forEach(function(h,i){
      if(!h.id){h.id='sect-'+i+'-'+h.tagName.toLowerCase();}
      var tag=h.tagName.toLowerCase();
      var link=document.createElement('a');
      link.href='#'+h.id;link.textContent=h.textContent.trim().substring(0,80);
      link.setAttribute('data-id',h.id);
      if(tag==='h1'){link.className='nav-h1';}
      if(tag==='h2'){link.className='nav-h2';link.style.paddingLeft='2rem';}
      if(tag==='h3'){link.className='nav-h3';link.style.paddingLeft='3rem';link.style.fontSize='.75rem';link.style.opacity='.8';}
      frag.appendChild(link);tocs.push({id:h.id,text:h.textContent.trim(),tag:tag});
    });
    NAV.innerHTML='';NAV.appendChild(frag);
    window.__toc=tocs;
  }

  /* ── Active Heading ─────────────────────────────── */
  function updateActive(){
    var pos=window.scrollY+SCROLL_OFFSET+20;
    var active=null;
    (window.__toc||[]).forEach(function(h){
      var el=document.getElementById(h.id);
      if(el&&el.offsetTop<=pos)active=h.id;
    });
    $$('#sidebar-nav a').forEach(function(a){a.classList.toggle('active',a.getAttribute('data-id')===active);});
  }

  /* ── Progress Bar ───────────────────────────────── */
  function updateProgress(){
    var pct=Math.min((window.scrollY/(document.documentElement.scrollHeight-window.innerHeight))*100,100);
    PROGRESS.style.width=pct+'%';
  }

  /* ── Search ─────────────────────────────────────── */
  var searchEl,searchIdx=[],searchVis=false;
  function initSearch(){
    searchEl=document.createElement('div');
    searchEl.className='search-results';
    searchEl.innerHTML='<div class="search-results-header">Results</div><div class="search-results-list"></div>';
    document.body.appendChild(searchEl);
    (window.__toc||[]).forEach(function(h,i){
      searchIdx.push({id:h.id,title:h.text,tag:h.tag,idx:i});
    });
    $('.sidebar-search input').addEventListener('input',debounce(function(e){
      var q=e.target.value.toLowerCase().trim();
      if(q.length<2){searchEl.classList.remove('visible');searchVis=false;return;}
      var hits=searchIdx.filter(function(r){return r.title.toLowerCase().indexOf(q)!==-1;}).slice(0,15);
      var list=searchEl.querySelector('.search-results-list');
      list.innerHTML='';
      if(!hits.length){list.innerHTML='<div class="search-result-item" style="color:var(--text3)">No matching sections</div>';}
      hits.forEach(function(r){
        var count=0;(window.__toc||[]).forEach(function(t){if(t.text.toLowerCase().indexOf(q)!==-1)count++;});
        var relevance=Math.round((1-(r.idx/(window.__toc||[]).length))*5);
        var bars='';for(var i=0;i<5;i++)bars+='<span style="opacity:'+(i<relevance?1:.2)+';height:'+(8+i*3)+'px"></span>';
        var a=document.createElement('a');
        a.className='search-result-item';a.href='#'+r.id;
        a.innerHTML='<span class="result-title">'+highlight(r.title,q)+'</span><span class="result-relevance">'+bars+'</span>';
        a.addEventListener('click',function(){searchEl.classList.remove('visible');searchVis=false;$('.sidebar-search input').value='';});
        list.appendChild(a);
      });
      searchEl.classList.add('visible');searchVis=true;
    },DEBOUNCE_MS));
    document.addEventListener('keydown',function(e){if((e.ctrlKey||e.metaKey)&&e.key==='k'){e.preventDefault();$('.sidebar-search input').focus();}});
    document.addEventListener('click',function(e){if(searchVis&&!searchEl.contains(e.target)&&!e.target.closest('.sidebar-search')){searchEl.classList.remove('visible');searchVis=false;}});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&searchVis){searchEl.classList.remove('visible');searchVis=false;}});
  }
  function highlight(t,q){var i=t.toLowerCase().indexOf(q.toLowerCase());if(i===-1)return t;return t.substring(0,i)+'<strong>'+t.substring(i,i+q.length)+'</strong>'+t.substring(i+q.length);}
  function debounce(fn,ms){var t;return function(){var a=arguments,c=this;clearTimeout(t);t=setTimeout(function(){fn.apply(c,a);},ms);};}

  /* ── Mobile ─────────────────────────────────────── */
  function initMobile(){
    $('.menu-toggle').addEventListener('click',function(){SIDEBAR.classList.toggle('open');OVERLAY.classList.toggle('visible');});
    OVERLAY.addEventListener('click',function(){SIDEBAR.classList.remove('open');OVERLAY.classList.remove('visible');});
    $$('#sidebar-nav a').forEach(function(a){a.addEventListener('click',function(){if(window.innerWidth<=1024){SIDEBAR.classList.remove('open');OVERLAY.classList.remove('visible');}});});
  }

  /* ── Collapsible Chapters ───────────────────────── */
  function initCollapse(){
    $$('#main-content h2').forEach(function(h2){
      if(/CONTENTS|HOW TO READ|READING PATHWAYS|CONCEPT MAP|NOTATION|HISTORICAL|PROLOGUE|ABSTRACT|QUICK REFERENCE|CHAPTER TRANSITION|INDEX|FURTHER READING|GLOSSARY|VERSION HISTORY/i.test(h2.textContent))return;
      h2.style.cursor='pointer';h2.setAttribute('data-collapsed','false');
      var icon=document.createElement('span');icon.style.cssText='font-size:.7em;color:var(--accent);margin-left:.3em';icon.textContent='▾';h2.appendChild(icon);
      h2.addEventListener('click',function(){
        var c=h2.getAttribute('data-collapsed')==='true';
        h2.setAttribute('data-collapsed',String(!c));
        var n=h2.nextElementSibling;
        while(n&&n.tagName!=='H2'){n.style.display=c?'':'none';n=n.nextElementSibling;}
        icon.textContent=c?'▾':'▸';
      });
    });
  }

  /* ── Back to Top ────────────────────────────────── */
  function initBackTop(){
    var btn=document.createElement('button');btn.className='back-to-top';btn.textContent='↑';btn.title='Back to top';
    btn.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
    document.body.appendChild(btn);
    addEventListener('scroll',function(){btn.classList.toggle('visible',window.scrollY>600);});
  }

  /* ── Smooth Scroll ──────────────────────────────── */
  function initSmoothScroll(){
    document.addEventListener('click',function(e){
      var link=e.target.closest('a[href^="#"]');
      if(!link||link.classList.contains('search-result-item'))return;
      var id=link.getAttribute('href').substring(1),el=document.getElementById(id);
      if(el){e.preventDefault();window.scrollTo({top:el.getBoundingClientRect().top+window.scrollY-SCROLL_OFFSET,behavior:'smooth'});}
    });
  }

  /* ── Section Anchors ────────────────────────────── */
  function initSectionAnchors(){
    $$('#main-content h2,#main-content h3,#main-content h4').forEach(function(h){
      var a=document.createElement('a');a.className='section-anchor';a.href='#'+h.id;a.textContent='#';a.title='Copy link to this section';
      a.addEventListener('click',function(e){e.preventDefault();navigator.clipboard.writeText(window.location.href.split('#')[0]+'#'+h.id).then(function(){a.textContent='✓';a.classList.add('copied');setTimeout(function(){a.textContent='#';a.classList.remove('copied');},1500);});});
      h.appendChild(a);
    });
  }

  /* ═══════════════════════════════════════════════════
     CONTENT-AWARE ENHANCEMENTS
     Read the DOM, identify content types, enhance.
     ═══════════════════════════════════════════════════ */

  /* ── Glossary Tooltips ──────────────────────────── */
  var glossary={};
  function buildGlossaryIndex(){
    var gl=$('#main-content').innerHTML.match(/<strong>(Adele ring|Archimedean metric|Bruhat[–-]Tits tree|Container|Monna projection|p-adic numbers|Projection artifact|Shift metric|Stabilizer code|Threshold principle|Tree automorphism|Ultrametric|Basin-crossing|Holographic principle|Product formula|Scrambling|Born rule|Decoherence|Riemann Hypothesis|Langlands program|Automorphic form|Measurement problem|Ball-inclusion tree|Lorentz symmetry|Adelic space|Coarse-graining)<\/strong>/gi);
    if(!gl)return;
    var defs={};
    var text=document.getElementById('main-content').textContent;
    gl.forEach(function(m){defs[m.replace(/<[^>]+>/g,'')]=true;});
    Object.keys(defs).forEach(function(term){
      var defStart=text.indexOf(term);
      if(defStart===-1)return;
      var defEnd=text.indexOf('.',defStart+term.length);
      if(defEnd===-1)defEnd=defStart+term.length+200;
      var snippet=text.substring(defStart,Math.min(defEnd+1,defStart+300)).trim();
      glossary[term.toLowerCase()]=snippet;
    });
  }
  function applyGlossaryTooltips(){
    buildGlossaryIndex();
    Object.keys(glossary).forEach(function(term){
      var lower=term.toLowerCase();
      document.querySelectorAll('#main-content p,#main-content li,#main-content td').forEach(function(el){
        if(el.querySelector('.glossary-term'))return;
        var html=el.innerHTML;
        var idx=html.toLowerCase().indexOf(lower);
        if(idx!==-1&&!html.substring(Math.max(0,idx-1),idx).match(/[a-z]/i)){
          var before=html.substring(0,idx);
          var match=html.substring(idx,idx+term.length);
          var after=html.substring(idx+term.length);
          el.innerHTML=before+'<span class="glossary-term" data-term="'+term+'">'+match+'</span>'+after;
        }
      });
    });
    document.querySelectorAll('.glossary-term').forEach(function(el){
      el.addEventListener('mouseenter',function(){
        var tip=document.createElement('div');tip.className='glossary-tooltip visible';
        tip.textContent=(glossary[el.getAttribute('data-term').toLowerCase()]||'Defined term — see Glossary').substring(0,250)+'…';
        el.appendChild(tip);
        el.addEventListener('mouseleave',function(){if(tip.parentNode)tip.parentNode.removeChild(tip);},{once:true});
      });
    });
  }

  /* ── Proof Collapsibility ───────────────────────── */
  function applyProofCollapse(){
    $$('#main-content p,#main-content div').forEach(function(el){
      if(el.classList.contains('proof-block'))return;
      var text=el.textContent||'';
      if(text.trim().match(/^Proof\.\s/)&&!el.closest('.proof-block')){
        var proofDiv=document.createElement('div');proofDiv.className='proof-block';
        var btn=document.createElement('button');btn.className='proof-toggle';
        var wc=0,n=el;while(n&&!n.textContent.match(/□/)){wc+=n.textContent.length;n=n.nextElementSibling;}
        var readTime=Math.max(1,Math.round(wc/200));
        btn.innerHTML='Proof <span style="font-size:.75em;color:var(--text3);margin-left:.5em">~'+readTime+' min read</span>';
        var body=document.createElement('div');body.className='proof-body';
        btn.addEventListener('click',function(){
          var open=body.classList.toggle('open');
          btn.classList.toggle('open',open);
          if(open&&window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([body]);
        });
        proofDiv.appendChild(btn);proofDiv.appendChild(body);
        el.parentNode.insertBefore(proofDiv,el);
        body.appendChild(el);var next=el.nextElementSibling;
        while(next&&(next.textContent||'').indexOf('□')===-1&&!next.matches('h1,h2,h3,h4')){
          var n2=next.nextElementSibling;body.appendChild(next);next=n2;
        }
        if(next&&(next.textContent||'').indexOf('□')!==-1)body.appendChild(next);
      }
    });
  }

  /* ── Diagram Zoom ───────────────────────────────── */
  function applyDiagramZoom(){
    $$('pre.diagram,pre:has(code)').forEach(function(pre){
      var code=pre.querySelector('code');
      if(!code)return;
      var text=code.textContent||'';
      if(/[┌┐└┘├┤┬┴┼│─═╔╗╚╝║╠╣╦╩╬▶▼▲◀◆◇○●□■☆★↑↓→←↗↘↙↖]/.test(text)&&text.split('\n').length>3){
        pre.classList.add('diagram');
        pre.addEventListener('click',function(e){
          if(e.target.closest('a'))return;
          pre.classList.toggle('zoomed');
        });
      }
    });
  }

  /* ── Equation Modal ─────────────────────────────── */
  function applyEquationModals(){
    var modal=document.createElement('div');modal.className='equation-modal';
    modal.innerHTML='<div class="equation-modal-content"></div><button class="equation-modal-close">×</button>';
    document.body.appendChild(modal);
    modal.querySelector('.equation-modal-close').addEventListener('click',function(){modal.classList.remove('visible');});
    modal.addEventListener('click',function(e){if(e.target===modal)modal.classList.remove('visible');});
    document.querySelectorAll('.MathJax_Display, mjx-container[mjx-display="true"]').forEach(function(eq){
      eq.style.cursor='pointer';
      eq.addEventListener('click',function(){
        var clone=eq.cloneNode(true);
        clone.style.fontSize='1.3em';
        modal.querySelector('.equation-modal-content').innerHTML='';
        modal.querySelector('.equation-modal-content').appendChild(clone);
        modal.classList.add('visible');
        if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([modal]);
      });
    });
  }

  /* ── Section Read Tracking ──────────────────────── */
  function applyReadTracking(){
    var read=new Set(JSON.parse(localStorage.getItem('read-sections')||'[]'));
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          var h=e.target.closest('h2');
          if(h&&h.id){read.add(h.id);localStorage.setItem('read-sections',JSON.stringify([...read]));}
        }
      });
    },{threshold:0.5});
    $$('#main-content h2').forEach(function(h){observer.observe(h);});
    read.forEach(function(id){
      var link=NAV.querySelector('a[data-id="'+id+'"]');
      if(link)link.classList.add('read');
    });
  }

  /* ── Boot ───────────────────────────────────────── */
  function init(){
    buildSidebar();
    initSearch();
    initMobile();
    initCollapse();
    initBackTop();
    initSmoothScroll();
    initSectionAnchors();
    /* scroll loop */
    var ticking=false;
    addEventListener('scroll',function(){if(!ticking){requestAnimationFrame(function(){updateActive();updateProgress();ticking=false;});ticking=true;}});
    /* theme buttons */
    $$('.theme-toggle,.theme-toggle-mobile').forEach(function(b){b.addEventListener('click',toggleTheme);});
    /* content-aware (deferred for performance) */
    setTimeout(function(){
      applyProofCollapse();
      applyDiagramZoom();
      applyReadTracking();
    },500);
    setTimeout(function(){
      applyGlossaryTooltips();
    },1000);
    setTimeout(function(){
      applyEquationModals();
    },2000);
    /* initial state */
    updateProgress();
    updateActive();
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
