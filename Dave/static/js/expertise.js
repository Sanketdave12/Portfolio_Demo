const btn_nav_head = document.querySelector('.nav-head');
let btn_nav_options = false;
const btn_nav_options = document.querySelector('.nav-options');
btn_nav_head.addEventListener('click', () => {
    if(!btn_nav_options){
        btn_nav_head.classList.add('show');
        btn_nav_options = true;
        console.log('Hiii')
    }
    else{
        btn_nav_head.remove('show');
        btn_nav_head = false;
    }
});