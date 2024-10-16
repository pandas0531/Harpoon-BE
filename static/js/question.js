window.onload = function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    
    const value = urlParams.get('value');
    const number = urlParams.get('number');

    const locationElement = document.getElementById('location');
    
    if (locationElement) {
        locationElement.innerText = `카테고리 > ${value} > ${number}번`;
    }

    const menuCategoryElement = document.getElementById('menu-category');
    if (menuCategoryElement) {
        menuCategoryElement.addEventListener('click', function() {
            const url = `category?value=${value}`;
            location.href = url;
        });
    }

    let answer = 9999; // 정답 

    const form = document.querySelector('.answer-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const input = document.querySelector('.answer-input');
            const feedback = document.getElementById('feedback');

            if (input && feedback) {
                if (input.value == answer) {
                    feedback.textContent = "맞았습니다.";
                    feedback.className = "message correct";
                } else {
                    feedback.textContent = `${input.value} : 틀렸습니다`;
                    feedback.className = "message wrong";
                }
            }
        });
    }
};