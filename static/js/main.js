document.addEventListener("DOMContentLoaded", function () {
  const sidebarWrapper = document.getElementById("sidebar-wrapper");
  const contentWrapper = document.querySelector(".content-wrapper");
  const toggleBtn = document.getElementById("toggle-sidebar");
  const homeBtn = document.querySelector(".home-btn");

  const sidebarItems = document.querySelectorAll(
    "#sidebar-wrapper .list-group-item"
  );
  const bottomNavItems = document.querySelectorAll(".bottom-nav-item");

  toggleBtn.addEventListener("click", function () {
    sidebarWrapper.classList.toggle("collapsed");
    contentWrapper.classList.toggle("expanded");
  });

  function setActiveItem(index) {
    if (index === bottomNavItems.length - 1) return;

    sidebarItems.forEach((item) => item.classList.remove("active"));
    if (sidebarItems[index]) sidebarItems[index].classList.add("active");

    bottomNavItems.forEach((item) => item.classList.remove("active"));
    if (bottomNavItems[index]) bottomNavItems[index].classList.add("active");
  }

  sidebarItems.forEach((item, index) => {
    item.addEventListener("click", function (e) {
      e.preventDefault();
      setActiveItem(index);
    });
  });

  bottomNavItems.forEach((item, index) => {
    if (index < bottomNavItems.length - 1) {
      item.addEventListener("click", function (e) {
        e.preventDefault();
        setActiveItem(index);
      });
    }
  });

  const userSection = document.getElementById("user-section");
  const userMenu = document.getElementById("user-menu");

  userSection.addEventListener("click", function (e) {
    userMenu.classList.toggle("show");
    e.stopPropagation();
  });

  const mobileUserBtn = document.getElementById("mobile-user-btn");
  const mobileUserMenu = document.getElementById("mobile-user-menu");

  mobileUserBtn.addEventListener("click", function (e) {
    e.preventDefault();
    mobileUserMenu.classList.toggle("show");
    e.stopPropagation();
  });

  document.addEventListener("click", function () {
    userMenu.classList.remove("show");
    mobileUserMenu.classList.remove("show");
  });

  userMenu.addEventListener("click", function (e) {
    e.stopPropagation();
  });

  mobileUserMenu.addEventListener("click", function (e) {
    e.stopPropagation();
  });
});
