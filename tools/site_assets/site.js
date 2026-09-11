/* BA Prompt Forge - progressive enhancement only.
   Every page is complete and usable with this file blocked: format panels are
   all rendered in the HTML, the prompt list is fully in the DOM, and nothing
   below adds content. It only hides, filters and copies. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  /* ---- theme ---------------------------------------------------------- */
  var root = document.documentElement;
  try {
    var saved = localStorage.getItem("bpf-theme");
    if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  } catch (e) { /* private mode: fall back to prefers-color-scheme */ }

  function currentTheme() {
    var set = root.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  Array.prototype.forEach.call(document.querySelectorAll(".theme-toggle"), function (btn) {
    function sync() {
      var dark = currentTheme() === "dark";
      btn.setAttribute("aria-pressed", String(dark));
      btn.textContent = dark ? "Light theme" : "Dark theme";
    }
    sync();
    btn.hidden = false;
    btn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("bpf-theme", next); } catch (e) { /* ignore */ }
      sync();
    });
  });

  /* ---- format tabs (WAI-ARIA tabs pattern, manual activation) ---------- */
  Array.prototype.forEach.call(document.querySelectorAll(".tabs"), function (group) {
    var tabs = Array.prototype.slice.call(group.querySelectorAll('[role="tab"]'));
    var panels = Array.prototype.slice.call(group.querySelectorAll('[role="tabpanel"]'));
    if (!tabs.length || tabs.length !== panels.length) return;

    function select(index, focus) {
      tabs.forEach(function (tab, i) {
        var on = i === index;
        tab.setAttribute("aria-selected", String(on));
        tab.tabIndex = on ? 0 : -1;
        panels[i].hidden = !on;
      });
      if (focus) tabs[index].focus();
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(i, false); });
      tab.addEventListener("keydown", function (event) {
        var next = null;
        switch (event.key) {
          case "ArrowRight": case "ArrowDown": next = (i + 1) % tabs.length; break;
          case "ArrowLeft": case "ArrowUp": next = (i - 1 + tabs.length) % tabs.length; break;
          case "Home": next = 0; break;
          case "End": next = tabs.length - 1; break;
          default: return;
        }
        event.preventDefault();
        select(next, true);
      });
    });

    group.hidden = false;
    select(0, false);
  });

  /* ---- copy to clipboard ---------------------------------------------- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-copy]"), function (btn) {
    var status = document.getElementById(btn.getAttribute("data-copy-status"));
    btn.hidden = false;
    btn.addEventListener("click", function () {
      var source = document.getElementById(btn.getAttribute("data-copy"));
      if (!source) return;
      var text = source.textContent;
      function done(ok) {
        if (!status) return;
        status.textContent = ok
          ? "Prompt copied to the clipboard."
          : "Could not copy automatically - select the text and copy it.";
        window.setTimeout(function () { status.textContent = ""; }, 6000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); },
                                                 function () { done(false); });
      } else {
        done(false);
      }
    });
  });

  /* ---- prompt filtering ----------------------------------------------- */
  var list = document.getElementById("prompt-list");
  if (!list) return;

  var rows = Array.prototype.slice.call(list.querySelectorAll("[data-prompt]"));
  var search = document.getElementById("filter-search");
  var selects = Array.prototype.slice.call(document.querySelectorAll("[data-filter]"));
  var count = document.getElementById("result-count");
  var empty = document.getElementById("no-results");
  var reset = document.getElementById("filter-reset");

  function apply() {
    var term = (search && search.value || "").trim().toLowerCase();
    var shown = 0;

    rows.forEach(function (row) {
      var ok = true;
      if (term && row.getAttribute("data-haystack").indexOf(term) === -1) ok = false;
      if (ok) {
        for (var i = 0; i < selects.length; i++) {
          var key = selects[i].getAttribute("data-filter");
          var want = selects[i].value;
          if (want && row.getAttribute("data-" + key) !== want) { ok = false; break; }
        }
      }
      row.hidden = !ok;
      if (ok) shown++;
    });

    if (count) {
      count.textContent = shown === rows.length
        ? "Showing all " + rows.length + " prompts."
        : "Showing " + shown + " of " + rows.length + " prompts.";
    }
    if (empty) empty.hidden = shown !== 0;
  }

  if (search) search.addEventListener("input", apply);
  selects.forEach(function (select) { select.addEventListener("change", apply); });
  if (reset) {
    reset.hidden = false;
    reset.addEventListener("click", function () {
      if (search) search.value = "";
      selects.forEach(function (select) { select.value = ""; });
      apply();
      if (search) search.focus();
    });
  }
  apply();
})();
