/**
 * THE ULTRAMETRIC PARADIGM — Interactive Engine
 * GitHub Pages | rwnq8.github.io/ultrametric-paradigm
 */
(function() {
  'use strict';

  // ── Configuration ──────────────────────────────────
  const CONFIG = {
    contentFile: '0.9.md',
    sidebarId: 'sidebar-nav',
    contentId: 'main-content',
    scrollOffset: 80,
    searchMinChars: 2,
    debounceMs: 300,
  };

  // ── State ──────────────────────────────────────────
  let headingsList = [];
  let searchIndex = [];
  let searchResultsEl = null;
  let searchVisible = false;

  // ── DOM References ─────────────────────────────────
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  // ── Theme ──────────────────────────────────────────
  function initTheme() {
    const saved = localStorage.getItem('ultrametric-theme');
    if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.setAttribute('data-theme', 'dark');
    }
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('ultrametric-theme', next);
    updateThemeIcon(next);
  }

  function updateThemeIcon(theme) {
    const btn = $('.theme-toggle');
    if (btn) btn.textContent = theme === 'dark' ? '☀️' : '🌙';
    const btnMobile = $('.theme-toggle-mobile');
    if (btnMobile) btnMobile.textContent = theme === 'dark' ? '☀️' : '🌙';
  }

  // ── Sidebar Navigation ─────────────────────────────
  function buildSidebar() {
    const nav = $(`#${CONFIG.sidebarId}`);
    if (!nav) return;

    const headings = $$('#main-content h1, #main-content h2, #main-content h3, #main-content h4');
    headingsList = [];

    const frag = document.createDocumentFragment();

    headings.forEach((h, idx) => {
      // Ensure ID exists
      if (!h.id) {
        h.id = 'heading-' + idx + '-' + h.tagName.toLowerCase();
      }

      const tag = h.tagName.toLowerCase();
      const isPart = h.textContent.trim().startsWith('PART');
      const cls = isPart || h.classList.contains('hero-title')
        ? 'nav-h1'
        : tag === 'h2' ? 'nav-h2'
        : tag === 'h3' ? 'nav-h3'
        : 'nav-h4';

      const a = document.createElement('a');
      a.href = '#' + h.id;
      a.className = cls;
      a.textContent = h.textContent.trim().substring(0, 80);
      a.setAttribute('data-heading-id', h.id);

      frag.appendChild(a);

      headingsList.push({
        id: h.id,
        text: h.textContent.trim(),
        tag: tag,
      });

      // Build search index
      searchIndex.push({
        id: h.id,
        title: h.textContent.trim(),
        section: tag.toUpperCase(),
      });
    });

    nav.innerHTML = '';
    nav.appendChild(frag);
  }

  // ── Active Heading Highlight ────────────────────────
  function updateActiveHeading() {
    const scrollPos = window.scrollY + CONFIG.scrollOffset + 10;
    const links = $$(`#${CONFIG.sidebarId} a`);

    let activeId = null;
    headingsList.forEach(h => {
      const el = document.getElementById(h.id);
      if (el && el.offsetTop <= scrollPos) {
        activeId = h.id;
      }
    });

    links.forEach(link => {
      if (link.getAttribute('data-heading-id') === activeId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  // ── Progress Bar ───────────────────────────────────
  function updateProgressBar() {
    const bar = $('.progress-bar');
    if (!bar) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = Math.min(progress, 100) + '%';
  }

  // ── Search ─────────────────────────────────────────
  function initSearch() {
    searchResultsEl = document.createElement('div');
    searchResultsEl.className = 'search-results';
    searchResultsEl.innerHTML = '<div class="search-results-header">Search Results</div><div class="search-results-list"></div>';
    document.body.appendChild(searchResultsEl);

    // Keyboard shortcut: Ctrl+K or /
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = $('.sidebar-search input');
        if (searchInput) searchInput.focus();
      }
    });

    // Close search on click outside
    document.addEventListener('click', (e) => {
      if (searchVisible && !searchResultsEl.contains(e.target) && !e.target.closest('.sidebar-search')) {
        hideSearch();
      }
    });

    // Close on Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && searchVisible) {
        hideSearch();
      }
    });
  }

  let searchTimeout;
  function performSearch(query) {
    clearTimeout(searchTimeout);
    if (!query || query.length < CONFIG.searchMinChars) {
      hideSearch();
      return;
    }

    searchTimeout = setTimeout(() => {
      const q = query.toLowerCase();
      const results = searchIndex.filter(item =>
        item.title.toLowerCase().includes(q)
      ).slice(0, 15);

      const listEl = searchResultsEl.querySelector('.search-results-list');
      listEl.innerHTML = '';

      if (results.length === 0) {
        listEl.innerHTML = '<div class="search-result-item" style="color:var(--text-secondary);">No results found for "' + escapeHtml(query) + '"</div>';
      } else {
        results.forEach(r => {
          const item = document.createElement('a');
          item.className = 'search-result-item';
          item.href = '#' + r.id;
          item.innerHTML = `
            <div class="result-title">${highlightMatch(r.title, q)}</div>
            <div class="result-excerpt">${r.section}</div>
          `;
          item.addEventListener('click', () => {
            hideSearch();
            const searchInput = $('.sidebar-search input');
            if (searchInput) searchInput.value = '';
          });
          listEl.appendChild(item);
        });
      }

      searchResultsEl.classList.add('visible');
      searchVisible = true;
    }, CONFIG.debounceMs);
  }

  function hideSearch() {
    searchResultsEl.classList.remove('visible');
    searchVisible = false;
  }

  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  function highlightMatch(text, query) {
    const idx = text.toLowerCase().indexOf(query.toLowerCase());
    if (idx === -1) return escapeHtml(text);
    return escapeHtml(text.substring(0, idx)) +
      '<strong>' + escapeHtml(text.substring(idx, idx + query.length)) + '</strong>' +
      escapeHtml(text.substring(idx + query.length));
  }

  // ── Collapsible Sections ───────────────────────────
  function initCollapsibleSections() {
    // Make chapter sections collapsible (h2 headings)
    const h2s = $$('#main-content h2');
    h2s.forEach(h2 => {
      // Skip non-collapsible headings
      if (h2.textContent.includes('CONTENTS') ||
          h2.textContent.includes('HOW TO READ') ||
          h2.textContent.includes('READING PATHWAYS') ||
          h2.textContent.includes('CONCEPT MAP') ||
          h2.textContent.includes('NOTATION AND CONVENTIONS') ||
          h2.textContent.includes('HISTORICAL NOTE') ||
          h2.textContent.includes('PROLOGUE') ||
          h2.textContent.includes('ABSTRACT') ||
          h2.textContent.includes('QUICK REFERENCE') ||
          h2.textContent.includes('CHAPTER TRANSITION')) {
        return;
      }

      h2.style.cursor = 'pointer';
      h2.setAttribute('data-collapsed', 'false');

      // Add toggle icon
      const icon = document.createElement('span');
      icon.className = 'collapse-icon';
      icon.textContent = ' ▾';
      icon.style.fontSize = '0.7em';
      icon.style.color = 'var(--accent)';
      h2.appendChild(icon);

      h2.addEventListener('click', () => {
        const collapsed = h2.getAttribute('data-collapsed') === 'true';
        h2.setAttribute('data-collapsed', String(!collapsed));

        // Hide/show all siblings until next h2
        let next = h2.nextElementSibling;
        while (next && next.tagName !== 'H2') {
          if (collapsed) {
            next.style.display = '';
          } else {
            next.style.display = 'none';
          }
          next = next.nextElementSibling;
        }

        icon.textContent = collapsed ? ' ▾' : ' ▸';
      });
    });
  }

  // ── Mobile Menu ────────────────────────────────────
  function initMobileMenu() {
    const toggleBtn = $('.menu-toggle');
    const sidebar = $('.sidebar');
    const overlay = $('.sidebar-overlay');

    if (!toggleBtn || !sidebar) return;

    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      if (overlay) overlay.classList.toggle('visible');
    });

    if (overlay) {
      overlay.addEventListener('click', () => {
        sidebar.classList.remove('open');
        overlay.classList.remove('visible');
      });
    }

    // Close sidebar when a nav link is clicked (mobile)
    $$(`#${CONFIG.sidebarId} a`).forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 1024) {
          sidebar.classList.remove('open');
          if (overlay) overlay.classList.remove('visible');
        }
      });
    });
  }

  // ── Back to Top ────────────────────────────────────
  function initBackToTop() {
    const btn = document.createElement('button');
    btn.className = 'back-to-top';
    btn.innerHTML = '↑';
    btn.title = 'Back to top';
    btn.style.cssText = `
      position: fixed; bottom: 5rem; right: 1.5rem;
      width: 44px; height: 44px; border-radius: 50%;
      background: var(--bg-card); border: 1px solid var(--border);
      box-shadow: var(--shadow); cursor: pointer;
      font-size: 1.3rem; display: flex; align-items: center; justify-content: center;
      z-index: 50; opacity: 0; transition: opacity 0.3s, transform 0.2s;
      color: var(--text-primary);
    `;
    document.body.appendChild(btn);

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', () => {
      btn.style.opacity = window.scrollY > 600 ? '1' : '0';
    });
  }

  // ── Smooth Scroll for Hash Links ───────────────────
  function initSmoothScroll() {
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href^="#"]');
      if (!link) return;
      const targetId = link.getAttribute('href').substring(1);
      const target = document.getElementById(targetId);
      if (target) {
        e.preventDefault();
        const offset = CONFIG.scrollOffset;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  }

  // ── Initialize ─────────────────────────────────────
  function init() {
    initTheme();
    buildSidebar();
    initSearch();
    initCollapsibleSections();
    initMobileMenu();
    initSmoothScroll();
    initBackToTop();

    // Update active heading on scroll
    let scrollTicking = false;
    window.addEventListener('scroll', () => {
      if (!scrollTicking) {
        requestAnimationFrame(() => {
          updateActiveHeading();
          updateProgressBar();
          scrollTicking = false;
        });
        scrollTicking = true;
      }
    });

    // Theme toggle buttons
    const themeBtn = $('.theme-toggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', toggleTheme);
      updateThemeIcon(document.documentElement.getAttribute('data-theme') || 'light');
    }

    const themeBtnMobile = $('.theme-toggle-mobile');
    if (themeBtnMobile) {
      themeBtnMobile.addEventListener('click', toggleTheme);
    }

    // Search input handler
    const searchInput = $('.sidebar-search input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        performSearch(e.target.value);
      });
    }

    // Initial progress bar
    updateProgressBar();

    console.log('🌳 The Ultrametric Paradigm — Interactive Engine Initialized');
  }

  // ── Boot ───────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
