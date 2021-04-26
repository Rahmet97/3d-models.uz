if (window.performance) {
    console.info("window.performance works fine on this browser");
    downloadCounter();
  }
  console.info(performance.navigation.type);
  if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
    console.info( "This page is reloaded" );
    downloadCounter();
  } else {
    console.info( "This page is not reloaded");
  }

  
  function downloadCounter(){
      console.log('Download Counter Method')
  
      var url = '/ajax/downloads/'
  
      fetch(url, {
          method:'POST',
          headers:{
              'Content-Type':'application/json',
              'Accept': 'application/json',
              'X-CSRFToken':csrftoken,
          },
      })
      .then((response) => {
         return response.json();
      })
      .then((data) => {
          var d_count = document.getElementById('Download_counted');
      
          console.log(data["instance"])
          d_count.innerHTML = data["instance"];
      });
  }
  
 