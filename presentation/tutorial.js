/* OS tabs are independent of slide navigation and accessible by keyboard. */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".tutorial-tabs").forEach(function (group) {
    const tabs = Array.from(group.querySelectorAll('[role="tab"]'));
    function select(tab) {
      tabs.forEach(function (item) {
        const active = item === tab;
        item.setAttribute("aria-selected", String(active));
        item.tabIndex = active ? 0 : -1;
        document.getElementById(item.getAttribute("aria-controls")).hidden = !active;
      });
      if (window.Reveal) Reveal.layout();
    }
    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () { select(tab); });
      tab.addEventListener("keydown", function (event) {
        if (["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) {
          event.preventDefault();
          event.stopPropagation();
          let next = event.key === "Home" ? 0 : event.key === "End" ? tabs.length - 1 :
            (index + (event.key === "ArrowRight" ? 1 : -1) + tabs.length) % tabs.length;
          select(tabs[next]);
          tabs[next].focus();
        }
      });
    });
  });
  document.querySelectorAll('a[href^="http"]').forEach(function (link) {
    link.target = "_blank";
    link.rel = "noopener noreferrer";
  });
  function reduceMotion() {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      Reveal.configure({transition: "none", backgroundTransition: "none"});
    }
  }
  if (window.Reveal) {
    if (Reveal.isReady()) reduceMotion();
    else Reveal.on("ready", reduceMotion);
  }
});
