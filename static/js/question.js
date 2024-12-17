// window.onload = function() {
//     const queryString = window.location.search;
//     const urlParams = new URLSearchParams(queryString);
    
//     const value = urlParams.get('value');
//     const number = urlParams.get('number');

//     const locationElement = document.getElementById('location');

//     const menuCategoryElement = document.getElementById('menu-category');
//     if (menuCategoryElement) {
//         menuCategoryElement.addEventListener('click', function() {
//             const url = `category?value=${value}`;
//             location.href = url;
//         });
//     }

//     let answer = 74; // 정답 

//     const form = document.querySelector('.answer-form');
//     if (form) {
//         form.addEventListener('submit', function(event) {
//             event.preventDefault();
            
//             const input = document.querySelector('.answer-input');
//             const feedback = document.getElementById('feedback');

//             if (input && feedback) {
//                 if (input.value == answer) {
//                     feedback.textContent = "맞았습니다.";
//                     feedback.className = "message correct";
//                 } else {
//                     feedback.textContent = `${input.value} : 틀렸습니다`;
//                     feedback.className = "message wrong";
//                 }
//             }
//         });
//     }
// };

window.onload = function() {
    // 현재 URL 가져오기
    const currentUrl = window.location.href;

    // URL을 '/' 기준으로 분리
    const parts = currentUrl.split('/');
    // 마지막 부분이 카테고리 번호
    const categoryNumber = parseInt(parts[parts.length - 1], 10); 

    let answer;

    // categoryNumber 값에 따라 answer값 설정
    switch (categoryNumber) {
        case 1:
            answer = 74;
            break;
        case 2:
            answer = 4;
            break;
        case 3:
            answer = 2;
            break;
        case 4:
            answer = 33;
            break;
        case 5:
            answer = 54;
            break;
        case 6:
            answer = 2;
            break;
        case 7:
            answer = 3;
            break;
        case 8:
            answer = 6;
            break;
        case 9:
            answer = 3;
            break;
        case 10:
            answer = 2;
            break;
        case 11:
            answer = 152;
            break;
        default:
            answer = 0; // 범위를 벗어났을 때 기본값
            break;
    }

    const form = document.querySelector('.answer-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const input = document.querySelector('.answer-input');
            const feedback = document.getElementById('feedback');

            if (input && feedback) {
                if (parseInt(input.value, 10) === answer) {
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
