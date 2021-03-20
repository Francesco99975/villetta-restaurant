let items = [];
let removeItemsButtons;
let clearBtn;
let continuetBtn;


var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
}

ready(() => { 
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'cart-items');
    xhr.send(null);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            res = JSON.parse(xhr.responseText);
            JSON.parse(res['items']).forEach(el => items.push({'id': el.pk, ...el.fields}));
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
                location.reload();
            } else {
                console.log("Response Error: " + bagXhr.status);
            }
        }
    };

    clrXhr = new XMLHttpRequest();

    clrXhr.onreadystatechange = () => {
        if(clrXhr.readyState == 4) {
            if(clrXhr.status == 200) {
                clrRes = JSON.parse(clrXhr.responseText);
                console.log(clrRes);
                location.reload();
            } else {
                console.log("Response Error: " + clrXhr.status);
            }
        }
    }

    clearBtn = document.querySelector('.clear-btn');
    clearBtn.addEventListener('click', (_) => {
        clrXhr.open('GET', 'clear-bag');
        clrXhr.send();
    });

    continuetBtn = document.querySelector('.continue-btn');

    removeItemButtons = document.querySelectorAll(".order-item"); 
    removeItemButtons.forEach((btn, index) => btn.addEventListener('click', (_) => {
        btn.remove();
        bagXhr.open('GET', `remove-from-bag/${items[index].id}`);
        bagXhr.send();    
    }));
});
