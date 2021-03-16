let orderItemButtons;
let items = [];

let orderedItems = [];

var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
}

ready(() => { 
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'items');
    xhr.send(null);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            res = JSON.parse(xhr.responseText);
            res['specials'].forEach(el => items.push(el.fields))
            res['antipasti'].forEach(el => items.push(el.fields))
            res['primi'].forEach(el => items.push(el.fields))
            res['secondi'].forEach(el => items.push(el.fields))
            res['pizze'].forEach(el => items.push(el.fields))
            res['desserts'].forEach(el => items.push(el.fields))
            res['beverages'].forEach(el => items.push(el.fields))
          } else {
            console.log('Error: ' + xhr.status); 
          }
        }
    };

    orderItemButtons = document.querySelectorAll(".order-item"); 
    orderItemButtons.forEach((btn, index) => btn.addEventListener('click', (_) => {
       orderedItems.push(items[index]);
       console.log(orderedItems);
    }));
});




