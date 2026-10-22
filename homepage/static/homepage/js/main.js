const year = document.querySelector("#current-year");
const menuButton = document.querySelector(".navbar-toggler");
const navigation = document.querySelector("#primaryNavigation");

if (year) {
  year.textContent = new Date().getFullYear();
}

if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const isExpanded = navigation.classList.toggle("show");
    menuButton.setAttribute("aria-expanded", String(isExpanded));
  });
}