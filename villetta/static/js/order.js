let items = [];
let orderItemsBtn;
let messages;
let message;
let checkoutBtn;


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
            res['specials'].forEach(el => items.push({'id': el.pk, ...el.fields}))
            res['antipasti'].forEach(el => items.push({'id': el.pk, ...el.fields}))
            res['primi'].forEach(el => items.push({'id': el.pk, ...el.fields}))
            res['secondi'].forEach(el => items.push({'id': el.pk, ...el.fields}))
            res['pizze'].forEach(el => items.push({'id': el.pk, ...el.fields}))
            res['desserts'].forEach(el => items.push({'id': el.pk, ...el.fields}))
            res['beverages'].forEach(el => items.push({'id': el.pk, ...el.fields}))
            checkoutBtn.setAttribute('data-count', res['bag-qty']);
          } else {
            console.log('Error: ' + xhr.status); 
          }
        }
    };

    const bagXhr = new XMLHttpRequest();

    bagXhr.onreadystatechange = () => {
        if(bagXhr.readyState == 4) {
            if(bagXhr.status == 200) {
                bagResponse = JSON.parse(bagXhr.responseText);
                message.innerHTML = bagResponse['message'];
                messages.classList.add('msg-open');
                checkoutBtn.setAttribute('data-count', bagResponse['bag-qty']);
                setTimeout(() => messages.classList.remove('msg-open'), 3000);
            } else {
                console.log("Response Error: " + bagXhr.status);
            }
        }
    };

    checkoutBtn = document.querySelector('.btn-checkout');
    messages = document.querySelector('.messages');
    message = document.querySelector('.message');

    orderItemButtons = document.querySelectorAll(".order-item"); 
    orderItemButtons.forEach((btn, index) => btn.addEventListener('click', (_) => {
        bagXhr.open('GET', `add-to-bag/${items[index].id}`);
        bagXhr.send();    
    }));
});

