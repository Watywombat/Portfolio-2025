/*=============== EMAIL JS ===============*/

const form = document.getElementById('contact-form');
const responseMessage = document.getElementById('contact-message'); // Fixed ID

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'Accept': 'application/json'
        }
    }).then(response => {
        if (response.ok) {
            responseMessage.textContent = 'Thank you for your message! I will get back to you soon.';
            form.reset(); 
        } else {
            responseMessage.textContent = 'There was a problem sending your message. Please try again.';
        }
    }).catch(error => {
        responseMessage.textContent = 'There was a problem sending your message. Please try again.';
    });
});

/*=============== SHOW SCROLL UP ===============*/ 

const scrollUp = ()=>{
    const scrollUp =document.getElementById('scroll-up')
    this.scrollY>= 350 ? scrollUp.classList.add('show-scroll')
                :scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll',scrollUp)

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/

const sections = document.querySelectorAll('section[id]');

const scrollActive = () => {
    const scrollDown = window.scrollY;
    sections.forEach(current => {
        const sectionHeight = current.offsetHeight,
              sectionTop = current.offsetTop - 58,
              sectionId = current.getAttribute('id'),
              sectionsClass = document.querySelectorAll('.nav__list a[href*=' + sectionId + ']');

        if (scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight) {
            sectionsClass.forEach(link => link.classList.add('active-link'));
        } else {
            sectionsClass.forEach(link => link.classList.remove('active-link'));
        }
    });
};

window.addEventListener('scroll', scrollActive);

window.addEventListener('scroll', scrollActive)
/*=============== SCROLL REVEAL ANIMATION ===============*/

const sr =ScrollReveal({
    origin:'top',
    distance: '60px',
    duration:2500,
    delay:400,
    //reset:true
}
)
sr.reveal(`.perfil, .contact__form`)
sr.reveal(`.info`,{origin:'left',delay:800})
sr.reveal(`.skills`,{origin:'left',delay:800})
sr.reveal(`.about`,{origin:'right',delay:1200})

sr.reveal(`.projects__card, .services__card, .experience__card, .section__title,.containers` ,{interval:200})
