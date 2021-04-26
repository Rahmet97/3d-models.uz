console.log("hello world")


function add_to_cart_view($this){
	var pk = $this.dataset.pk
	var pageid = $this.dataset.pageid
	var action = $this.dataset.action

	console.log('productPk: ', pk, 'Action:', action)
	console.log('USER: ', user)
	
	console.log('page: ', pageid)

	if (user == 'AnonymousUser'){
		LoginSignUpFunction(pk)
		console.log("User is not logged in")
	}else{
		console.log("User is logged in")
		updateUserOrder(pk, action, pageid)
	}	
}


function updateUserOrder(pk, action, pageid){
	console.log('User is authenticated, sending data...')

	var url = '/ajax/cart/detail/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'Accept': 'application/json',
			'X-CSRFToken':csrftoken,
		}, 
		body:JSON.stringify({'pk':pk, 'action':action, 'pageid':pageid})
	})
	.then((response) => {
	   return response.json();
	})
	.then((data) => {
		var notif_tag = document.getElementById('AlreadyAdded'+pk.toString());
	
		if(pageid == "cart-page"){
			location.reload()
		}
		// location.reload()
		console.log("action: ", data["done_action"])
		if (notif_tag != null){
			if (data["added"] == true && pageid == "product-page"){
				notif_tag.innerHTML = 'Added To Cart';
				notif_tag.classList.toggle("show");
			}
			if (data["already_added"] == true && pageid == "product-page"){
				notif_tag.innerHTML = 'Already Added';
				notif_tag.classList.toggle("show");
			}
		}
	});
}

// When the user clicks on div, open the popup
function LoginSignUpFunction(pk) {
	console.log("This method works fine")
	var popup = document.getElementById("PopupNotification"+pk.toString());
	popup.classList.toggle("show");
  }


function product_price($this){
	var price = $this.dataset.price;
	var price_info = $this.dataset.priceinfo;
	var display_price = document.getElementById("ProductPrice");
	var display_price_info = document.getElementById("ProductPriceInfo");
	display_price.innerHTML = price;
	display_price_info.innerHTML = price_info;

	console.log(price, price_info);
}


// control checkbox in cart page
function model_checkbox($this){
	var pk = $this.dataset.pk;
	var checkbox;
	var action = 'None';
	if (pk == 'all'){
		checkbox = document.getElementById('all_checkbox');
		if (checkbox.checked){
			action = 'checked';
		}else{
			action = 'unchecked';
		}
	}else{
		id = document.getElementById('model_checkbox'+toString(pk));
	}
	console.log(action);

	console.log(pk)
	total_price(pk, action)
	
}

// change total price in the cart page when checkbox sellected
function total_price(pk, action){
	$.ajax({
		type: 'GET',
		url: '/ajax/model/checkbox/',
		data : { 
			'pk':pk, 'action':action
		},
		success: function(response) {
			var instance = JSON.parse(response["instance"]);
			console.log("Sellected: ", instance.length);
			console.log("Sellected: ", instance);
			var total_price = 0.0;
			var mpk;
			var single_price;
			var m_checkbox;
			var all_checkbox = 0;

			if (instance.length > 0){
				document.getElementById("all_checkbox").type = "checkbox";
				for (var i = 0; i < instance.length; i++){
					console.log("pk: ",           instance[i]['pk']);
					console.log("cart_field: ",   instance[i]['fields']['cart_field']);
					mpk = instance[i]['pk']
					single_price = document.getElementById('single_price'+mpk).value;
					m_checkbox   = document.getElementById('single_price'+mpk) 
					if (instance[i]['fields']['cart_field']){
						console.log("Single price", single_price)
						total_price += parseFloat(single_price);
						all_checkbox ++;
						m_checkbox.checked = true;
					}else{
						m_checkbox.checked = false;
					}
				}
				console.log("Total price", total_price)
				model_total_price = document.getElementById("model_total_price")
				model_total_price.innerHTML = (total_price)
				if (all_checkbox ==  instance.length){
					document.getElementById("all_checkbox").checked = true;
				}else{
					document.getElementById("all_checkbox").checked = false;
				}
			}else{
				document.getElementById("all_checkbox").type = "hidden";
			}
		},
		error: function() { 
			console.log('Houston, we have a problem!');
		}
	});
}

// change checkbox in the cart page when page uploaded
function selected_models_info(){
	var pk = ''
	var action = ''

	$.ajax({
		type: 'GET',
		url: '/ajax/model/checkbox/',
		data : { 
			'pk':pk, 'action':action
		},
		success: function(response) {
			var instance = JSON.parse(response["instance"]);
			console.log("Sellected: ", instance.length);
			console.log("Sellected: ", instance);
			var all_checkbox = 0;
			if (instance.length > 0){
				document.getElementById("all_checkbox").type = "checkbox";
				for (var i = 0; i < instance.length; i++){
					mpk = instance[i]['pk'];
					var m_checkbox = document.getElementById('single_price'+mpk);

					if (instance[i]['fields']['cart_field']){
						m_checkbox.checked=true;
						all_checkbox ++;
					}else{
						m_checkbox.checked=false;
					}
				}
				if (all_checkbox ==  instance.length){
					document.getElementById("all_checkbox").checked = true;
				}else{
					document.getElementById("all_checkbox").checked = false;
				}
			}else{
				document.getElementById("all_checkbox").type = "hidden";
			}
			console.log("al", all_checkbox)
		},
		error: function() { 
			console.log('Houston, we have a problem!');
		}
	});
}
