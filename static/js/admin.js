window.onload = function() {
    const form = document.querySelector('.admin-form');
    const imageInput = document.getElementById('question-image');
    const imagePreview = document.getElementById('image-preview');
    const imageDisplay = document.getElementById('image-display');

    imageInput.addEventListener('change', function() {
        const file = this.files[0];

        if (file) {
            const reader = new FileReader();
            reader.onload = function(event) {
                imageDisplay.setAttribute('src', event.target.result);
                imageDisplay.style.display = 'block';
                imagePreview.querySelector('span').style.display = 'none';
            };
            reader.readAsDataURL(file);
        } else {
            imageDisplay.style.display = 'none';
            imagePreview.querySelector('span').style.display = 'block';
        }
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const title = document.getElementById('question-title').value;
        const answer = document.getElementById('question-answer').value;
        const content = document.getElementById('question-content').value;
        const imageFile = imageInput.files[0];

        console.log('문제 제목:', title);
        console.log('문제 정답:', answer);
        console.log('문제 내용:', content);

        if (imageFile) {
            console.log('문제 이미지 파일 이름:', imageFile.name);
            console.log('문제 이미지 파일 크기:', imageFile.size);
            console.log('문제 이미지 파일 형식:', imageFile.type);
        } else {
            console.log('문제 이미지가 업로드되지 않았습니다.');
        }
    });
};
