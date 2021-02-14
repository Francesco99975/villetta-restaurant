const menu = document.querySelector('.toggle-button');
const mobileNav = document.querySelector(".mobile-nav");
const backdrop = document.querySelector(".backdrop");

const mobileLinks = document.querySelectorAll(".mobile-nav__item");


if(mobileLinks) {
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            if(backdrop.classList.contains('open')) {
                setTimeout(function() {
                    backdrop.classList.toggle('open');
                }, 200);
                backdrop.style.display = 'none';
            }
            if(mobileNav.classList.contains('open')) mobileNav.classList.toggle('open');
        });
    });
} 

if(menu && mobileNav && backdrop) {
    backdrop.addEventListener('click', (event) => {
        if(backdrop.classList.contains('open')) {
            setTimeout(function() {
                backdrop.classList.toggle('open');
            }, 200);
            backdrop.style.display = 'none';
        }
        if(mobileNav.classList.contains('open')) mobileNav.classList.toggle('open');
    });

    menu.addEventListener('click', (event) => {
        backdrop.style.display = 'block';
        setTimeout(function() {
            backdrop.classList.toggle('open');
        }, 10);
        mobileNav.classList.toggle('open');
    });
}