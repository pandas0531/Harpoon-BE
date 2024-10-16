window.onload = function() {
    
    const loader = document.createElement('div');
    loader.style.position = 'fixed';
    loader.style.top = '0';
    loader.style.left = '0';
    loader.style.width = '100%';
    loader.style.height = '100%';
    loader.style.backgroundColor = '#ffffff';
    loader.style.zIndex = '9999';
    loader.style.display = 'flex';
    loader.style.justifyContent = 'center';
    loader.style.alignItems = 'center';
    loader.innerHTML = '<h1>수학을 켜다 | Onsoo</h1>';
    document.body.appendChild(loader);

    setTimeout(function() {
        loader.style.transition = 'opacity 0.5s ease'; 
        loader.style.opacity = '0';
        setTimeout(function() {
            document.body.removeChild(loader);
        }, 1000); 
    }, 800); 

    const logoImg = document.querySelector('.menu-img');
    logoImg.addEventListener('click', function() {
        location.href = '/';
    });

    const loginElement = document.querySelector('.menu-login');
    loginElement.addEventListener('click', function() {
        location.href = '/login';
    });

    const startButton = document.querySelector('.start-btn');
    startButton.addEventListener('click', function() {
        location.href = '/';
    });
};