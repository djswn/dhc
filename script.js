function toggleMenu() {
    var x = document.getElementById("nav-links");
    if (x.className === "nav-links") {
        x.className += " responsive";
    } else {
        x.className = "nav-links";
    }
}

function showPage(pageId) {
    var pages = document.getElementsByClassName("page");
    for (var i = 0; i < pages.length; i++) {
        pages[i].style.display = "none";
    }
    document.getElementById(pageId).style.display = "block";
}

// 초기화: 첫 페이지를 보이게 설정
document.addEventListener("DOMContentLoaded", function() {
    showPage('home');
});
