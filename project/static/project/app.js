$(document).ready(function(){
/*    $(".showcharts").click(function(){
    	var id=$(this).attr("id"); 
    	$.ajax({ 
    		dataType: "json",
    		type: "POST", 
    		url: "{% url 'shop:index'%}",     
    		data: {id},
    		success: function(json){
    			charts(json,"ColumnChart");
    		}
    	});
    });*/

    var d = new Date();
    var month = d.getMonth()+1;
    var day = d.getDate();
    var output = d.getFullYear() + '-' +
        (month<10 ? '0' : '') + month + '-' +
        (day<10 ? '0' : '') + day;


//init datepicker jQueryUI
    $( ".datepicker" ).val(output);    

// hightlighting certain client in table
    $(".visitor-row").click(function(){   
        $(this).addClass("selected").siblings().removeClass("selected");
        var visit = $(".selected > .visitor-login").text();
        $("#id_id_client").val(visit);
    });

//showing all visits of certain client
    $(".client-row").click(function(){  
        var id=$(this).attr("id"); 
        // alert(id);
        $.ajax({ 
            dataType: "json",
            type: "POST",
            url: 'clientDetail/', 
            // url: '{% url "welcome:clientDetail" %}', 
            // data: {id},
            data : { cl_id : $(this).attr("id") },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },

            success: function(json){
                visitTable(json);
            },

            error: function(json){
                alert('request failed');
            }
        });
    });

// CHARTS showcase
    $(".get_to_da_JSON").click(function(){ 
        var id1=$( "#dateRange1" ).val(); 
        var id2=$( "#dateRange2" ).val(); 
        // alert(id);
        $.ajax({ 
            dataType: "json",
            type: "POST",
            url: '/shop/charts_get/', 
            // url: '{% url "welcome:clientDetail" %}', 
            data: {id1, id2},
            // data : { cl_id : $(this).attr("id") },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },

            success: function(json){
                ChartVisitTotal(json,"ColumnChart");
            },

            error: function(json){
                alert('request failed');
            }
        });
    });

// autocomplete for sales
    $("#id_id_client").keyup(function(){  
        $.ajax({
            dataType: "json",
            type: "POST",
            url: "clientAutoComplete/",
            data:{keyword : $(this).val()},
            beforeSend: function(xhr, settings){
                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
                // $("#clients").css("background","#FFF url(LoaderIcon.gif) no-repeat 165px");
            },
            success: function(data){
                $("#clients_list").show();
                clientTable(data);
                $("#clients").css("background","#FFF");
            },
            error: function(json){
                alert('request failed');
            }
        });
    });

    $( ".datepicker" ).datepicker({
        dateFormat:"yy-mm-dd"
        // dateFormat:"DD, d MM, yy"
    });
    $( "#tabs" ).tabs();
});





//--------------------------------------
// FUNCTIONS 
//--------------------------------------






function clientTable(json){
    var tmp = "<table border=\"1\"><tr><td>Имя</td><td>Телефон</td><td>Возраст</td></tr>";
    for (var i = 0; i < json.listVal.length; i++) {
            tmp = tmp + 
                "<tr class=\"visitor-row\" id="+json.listVal[i].id+">" +
                    "<th class=\"visitor-login\">" + json.listVal[i].Login + "</th>" +
                    "<th>" + json.listVal[i].Phone + "</th>" +
                    "<th>" + json.listVal[i].Birthdate + "</th>" +
                "</tr> "    
    };
    tmp = tmp + "</table>";
    $(".layer").html(tmp);
    $(".visitor-row").click(function(){
        $(this).addClass("selected").siblings().removeClass("selected");
        var visit = $(".selected > .visitor-login").text();
        $("#clients").val(visit);
    });
};



function visitTable(json){
    var tmp = "<table border=\"1\"><tr><td>Имя</td><td>Дата</td><td>Событие</td></tr>";
    for (var i = 0; i < json.listVal.length; i++) {
            tmp = tmp + 
                "<tr>" +
                    "<th>" + json.listVal[i].id_client__login + "</th>" +
                    "<th>" + json.listVal[i].date + "</th>" +
                    "<th>" + json.listVal[i].id_event__name + "</th>" +
                "</tr> "    
    };
    tmp = tmp + "</table>";
    $(".layer").html(tmp);
};
        
function ChartVisitTotal(json,ChartType)
{
	var c=ChartType;
	var jsonData=json;
	google.load("visualization", "1", {packages:["corechart"], callback:drawVisualization});

	function drawVisualization()
	{
		var data = new google.visualization.DataTable();
		data.addColumn('string', 'Dates');
		data.addColumn('number', 'Visits');

		$.each(jsonData, function(i,jsonData)
		{
			var value=parseFloat(jsonData.visits);
			var name=jsonData.date;
			data.addRows([ [name, value]]);
		});


		var options = {
			title : "Общее количество посещений",
            is3D: true, //Pie Charts
            colors : ['#54C492','#f96302' ], //Bar of Pie Charts
            animation:{
            	duration: 3000,
            	easing: 'out',
            	startup: true
            },
        vAxis: {title: "Количество посещений"}, //Bar of Pie Charts
        hAxis: {title: "Даты посещений "}, //Bar of Pie Charts
        colorAxis: {colors: ['#54C492', '#cc0000']}, //Geo Charts
        datalessRegionColor: '#dedede', //Geo Charts
        defaultColor: '#dedede' //Geo Charts
    };

    var chart;
       if(c=="ColumnChart") // Column Charts
       	chart=new google.visualization.ColumnChart(document.getElementById('chart_div'));
       else if(c=="PieChart") // Pie Charts
       	chart=new google.visualization.PieChart(document.getElementById('piechart_div'));
       else if(c=="BarChart") // Bar Charts
       	chart=new google.visualization.BarChart(document.getElementById('bar_div'));

       chart.draw(data, options);
   }
}



