function tableFilter(){
		var input, filter, table, tr,td, i,txtValue;
		input = document.getElementById("myInput");
		
		//filter is the variable defined by the input in uppercase
		filter = input.value.toUpperCase();
		table = document.getElementById("myTable");
		tr = table.getElementsByTagName("tr");
		console.log(filter);
		
		for(i=0; i < tr.length; i++){
			td =tr[i].getElementsByTagName("td")[0];
			if(td){
				txtValue=td.textContent||td.innerText;
				
				//if name starts with letters input by the filter, then the table row is output
				if(txtValue.toUpperCase().startsWith(filter)){
					tr[i].style.display="";
					}else{
					tr[i].style.display = "none"
					}
				}
			}
	}