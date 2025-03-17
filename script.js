document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById('menu-icon');
    const sidebar = document.getElementById('sidebar');
    const homeSection = document.querySelector('.home-section');

    // Обработка клика на иконку меню
    if (menuIcon && sidebar && homeSection) {
        menuIcon.addEventListener('click', () => {
            menuIcon.classList.toggle('active');
            sidebar.classList.toggle('active');
            homeSection.classList.toggle('active');
        });
    }

    // Скрыть спиннер после загрузки страницы
    window.addEventListener('load', function () {
        document.body.classList.add('loaded');
    });

    // Плавный скролл для всех якорных ссылок
    document.querySelectorAll('.nav-links a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault(); // Отменяем стандартное поведение ссылки
            const target = document.querySelector(this.getAttribute('href')); // Получаем целевой элемент
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth' // Плавный скролл
                });
            }
        });
    });

    // Плавный показ элементов при прокрутке
    const restaurantItems = document.querySelectorAll('.restaurant-item');
    if (restaurantItems.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.1 // Элемент показывается, когда 10% его видно
        });

        restaurantItems.forEach(item => {
            observer.observe(item);
        });
    }
});