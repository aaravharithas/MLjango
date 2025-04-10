// ---
const hamMenuBtn = document.querySelector('#nav-dropdown-cont')
const smallMenu = document.querySelector('.dropdown-nav')
const headerHamMenuBtn = document.querySelector('.nav-dropdown')
const headerHamMenuCloseBtn = document.querySelector(
  '.nav-dropdown-close'
)
const headerSmallMenuLinks = document.querySelectorAll('.nav-dropdown-link')

hamMenuBtn.addEventListener('click', () => {
  if (smallMenu.classList.contains('dropdown-nav--active')) {
    smallMenu.classList.remove('dropdown-nav--active')
  } else {
    smallMenu.classList.add('dropdown-nav--active')
  }
  if (headerHamMenuBtn.classList.contains('d-none')) {
    headerHamMenuBtn.classList.remove('d-none')
    headerHamMenuCloseBtn.classList.add('d-none')
  } else {
    headerHamMenuBtn.classList.add('d-none')
    headerHamMenuCloseBtn.classList.remove('d-none')
  }
})

for (let i = 0; i < headerSmallMenuLinks.length; i++) {
  headerSmallMenuLinks[i].addEventListener('click', () => {
    smallMenu.classList.remove('dropdown-nav--active')
    headerHamMenuBtn.classList.remove('d-none')
    headerHamMenuCloseBtn.classList.add('d-none')
  })
}

// ---
const headerLogoConatiner = document.querySelector('#hero-home-profile-cont')

headerLogoConatiner.addEventListener('click', () => {
  location.href = '/'
})
;
