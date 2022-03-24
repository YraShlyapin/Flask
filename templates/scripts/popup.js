//неиспользуется пока
const popup_links = document.querySelectorAll(".popup_link")
const popup_close = document.querySelectorAll(".popup_close")

for (const popupLink of popup_links){
    popupLink.addEventListener("click",function(e){
        const name = popupLink.getAttribute('value')
        const current = document.getElementById(name)
        current.classList.add("open")
        document.body.style.overflow = "hidden"
    })
}

for (const popupCloseNow of popup_close){
    popupCloseNow.addEventListener("click",function(e){
        const name = popupCloseNow.getAttribute('value')
        const current = document.getElementById(name)
        current.classList.remove('open')
        document.body.style.overflow = "auto"
    })
}