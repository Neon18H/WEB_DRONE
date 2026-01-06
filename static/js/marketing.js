const initReveal = () => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
};

const initSmoothScroll = () => {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (event) => {
      const targetId = anchor.getAttribute("href");
      if (!targetId || targetId === "#") {
        return;
      }
      const target = document.querySelector(targetId);
      if (target) {
        event.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });
};

const initClock = () => {
  const clock = document.getElementById("dronexClock");
  if (!clock) {
    return;
  }
  const updateClock = () => {
    const now = new Date();
    const time = now.toLocaleTimeString("en-GB", { hour12: false });
    clock.textContent = time;
  };
  updateClock();
  setInterval(updateClock, 1000);
};

document.addEventListener("DOMContentLoaded", () => {
  initReveal();
  initSmoothScroll();
  initClock();
});
