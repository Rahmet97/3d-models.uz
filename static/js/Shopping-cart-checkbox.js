console.log("Hello this page is card page")
    
    
    
    
    
    let elProductName = document.querySelectorAll('.shopproduct__info--title')
    let elProductSum = document.querySelectorAll(".shopproduct__info b");
    let result = document.querySelector(".shopingcard__item--summ span");
    let elInputShoppingChecked = document.querySelector('.input__shopping-checkbox');
    let elShoppingNew = document.querySelector('.shopping__price-new')
    let checks = document.querySelectorAll(".all");
    let elCardItems = document.querySelectorAll('.card_items')
    
    let S = 0;
    elProductSum.forEach((sum, index) => {
      S +=parseFloat(sum.textContent, 10  )
    })
    
    elInputShoppingChecked.addEventListener('click', function(){
      if(elInputShoppingChecked.checked){
        elShoppingNew.textContent = S;
        elCardItems.forEach(function(element){
          element.checked = true;
        })

        resultsPriceCheked();
      }
      if(elInputShoppingChecked.checked == false){
        elShoppingNew.innerHTML = 0;
        elCardItems.forEach(function(element){
          element.checked = false;
        })
        
          resultsPrice()

      }
    })
    let elementSum = S;
    function resultsPriceCheked(){
      let NewSum = elementSum;
      elCardItems.forEach(function(element, index){
        
        element.addEventListener('click', function(evt){
          let elResultsNew = evt.target.parentElement.parentElement.children[2].children[0].children[0].textContent;
          if(element.checked) {
            NewSum +=parseFloat(elResultsNew, 10);
            elShoppingNew.textContent = NewSum;  
            // elInputShoppingChecked.checked = true
            if(NewSum == S){
              elInputShoppingChecked.checked = true
            }
          }
          if(element.checked === false){
            NewSum -=parseFloat(elResultsNew, 10);
            elShoppingNew.textContent = NewSum;
            elInputShoppingChecked.checked = false;
            if(NewSum == S){
              elInputShoppingChecked.checked = true
            }
          }
          
        })
      })
    }

    function resultsPrice(){
      let sumElementNew = 0;
      elCardItems.forEach(function(element, index){
        
        element.addEventListener('click', function(evt){
          let elResultsNew = evt.target.parentElement.parentElement.children[2].children[0].children[0].textContent;
          if(element.checked) {
            sumElementNew +=parseFloat(elResultsNew, 10);
            elShoppingNew.textContent = sumElementNew;  
            if(sumElementNew == S){
              elInputShoppingChecked.checked = true;
            }else{
              elInputShoppingChecked.checked = false;
            }
          }
          if(element.checked === false){
            sumElementNew -=parseFloat(elResultsNew, 10);
            elShoppingNew.textContent = sumElementNew;
            if(sumElementNew == S){
              elInputShoppingChecked.checked = true;
            }else{
              elInputShoppingChecked.checked = false;
            }
          }
          
        })
      })
    }

// {/* //  -------------------------------------------------------- */}

function resultsPriceWindow(){
      let sumElementWindow = 0;
      elCardItems.forEach(function(element, index){
        
        element.addEventListener('click', function(evt){
          let elResultsNew = evt.target.parentElement.parentElement.children[2].children[0].children[0].textContent;
          console.log(elResultsNew)
          if(element.checked) {
            sumElementWindow +=parseFloat(elResultsNew, 10);
            elShoppingNew.textContent = sumElementWindow;
            console.log(sumElementWindow);
            if(sumElementWindow == S){
              elInputShoppingChecked.checked = true;
            }else{
              elInputShoppingChecked.checked = false;
            }
          }
          if(element.checked === false){
            sumElementWindow -=parseFloat(elResultsNew, 10);
            elShoppingNew.textContent = sumElementWindow;
            if(sumElementWindow == S){
              elInputShoppingChecked.checked = true;
            }else{
              elInputShoppingChecked.checked = false;
            }
          }
          
        })
      })
    }
    
    resultsPriceWindow();
  