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


    $( ".datepicker" ).datepicker({
        dateFormat:"yy-mm-dd"
        // dateFormat:"DD, d MM, yy"
    });
    $( "#tabs" ).tabs();

//init datepicker jQueryUI
    $( ".datepicker #id1" ).val(output);   
    $( ".datepicker #id2" ).val(output);   
    $( ".datepicker #id11" ).val(output);   
    $( ".datepicker #id12" ).val(output);   

     $("#myCarousel").carousel();

// hightlighting certain client in table
    $(".visitor-row").click(function(){   
        $(this).addClass("selected").siblings().removeClass("selected");
        var visit = $(".selected > .visitor-login").text();
        $("#id_id_client").val(visit);
    });

// hightlighting certain PRODUCT in table
    $(".product-row").click(function(){   
        $(this).addClass("selected").siblings().removeClass("selected");
        var visit = $(".selected > .product-name").text();
        $("#id_id_product").val(visit);
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

// Visits CHARTS
    $(".get_to_da_JSON").click(function(){ 
        var id1=$( "#dateRange1" ).val(); 
        var id2=$( "#dateRange2" ).val(); 
        values = {"id1":id1, "id2":id2};
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
                ChartVisitTotal(json);
            },

            error: function(json){
                alert('request failed');
            }
        });
    });

// SALES charts
    $(".chart_sales").click(function(){ 
        var id11=$( "#dateRange11" ).val(); 
        var id12=$( "#dateRange12" ).val(); 
        $.ajax({ 
            dataType: "json",
            type: "POST",
            url: '/shop/charts_get1/', 
            // url: '{% url "welcome:clientDetail" %}', 
            data: {id11, id12},
            // data : { cl_id : $(this).attr("id") },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },

            success: function(json){
                ChartVisitTotal1(json,"ColumnChart");
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


});





//--------------------------------------
// FUNCTIONS 
//--------------------------------------






function clientTable(json){
    var tmp = "<table class=\"table table-bordered\"><tr class=\"tableHead\"><td>Имя</td><td>Сайт</td><td>Дата рождения</td></tr>";
    for (var i = 0; i < json.listVal.length; i++) {
            tmp = tmp + 
                "<tr class=\"visitor-row\" id="+json.listVal[i].id+">" +
                    "<th class=\"visitor-login\">" + json.listVal[i].ShortName + "</th>" +
                    "<th>" + json.listVal[i].Site + "</th>" +
                    "<th>" + json.listVal[i].Birthdate + "</th>" +
                "</tr> "    
    };
    tmp = tmp + "</table>";
    $(".layer").html(tmp);
    $(".visitor-row").click(function(){
        $(this).addClass("selected").siblings().removeClass("selected");
        var visit = $(".selected > .visitor-login").text();
        $("#id_id_client").val(visit);
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
        
function ChartVisitTotal(json)
{
	var jsonData=json;
	// google.load("visualization", "1", {packages:["corechart"], callback:drawVisualization});
    google.charts.load('current', {packages:['corechart']});
    google.charts.setOnLoadCallback(drawVisualization);
	function drawVisualization()
	{
		var data = new google.visualization.DataTable();
		data.addColumn('string', 'Dates');
		data.addColumn('number', 'Посещения');

		$.each(jsonData, function(i,jsonData)
		{
			var value=parseFloat(jsonData.visits);
			var name=String(jsonData.Date);
			data.addRows([[name, value]]);
		});

		var options = {
			title : "Общее количество посещений",
            colors : ['#16a67f' ], //Bar of Pie Charts
            // width: 500,
            height: 400,
            legend: 'none',
            animation:{
            	duration: 1500,
            	easing: 'out',
            	startup: true
            },
            vAxis: {title: "Количество посещений", gridlines: { count: 4 }}, //Bar of Pie Charts
            hAxis: {title: "Даты посещений ", showTextEvery: 7},
            defaultColor: '#dedede' //Geo Charts
        };
        var chart;
        chart=new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, options);
    }
}


function ChartVisitTotal1(json,ChartType)
{
    var c=ChartType;
    var jsonData=json;
    google.load("visualization", "1", {packages:["corechart"], callback:drawVisualization1});

    function drawVisualization1()
    {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Даты');
        data.addColumn('number', 'Число продаж');

        $.each(jsonData, function(i,jsonData)
        {
            var value=parseFloat(jsonData.sales);
            var name=jsonData.Date;
            data.addRows([ [name, value]]);
        });


        var options = {
            title : "Общее количество продаж",
            colors : ['#16a67f' ], //Bar of Pie Charts
            // width: 500,
            height: 400,
            legend: 'none',
            animation:{
                duration: 1500,
                easing: 'out',
                startup: true
            },
            vAxis: {title: "Количество посещений", gridlines: { count: 4 }}, //Bar of Pie Charts
            hAxis: {title: "Даты посещений ", showTextEvery: 7},
            defaultColor: '#dedede' //Geo Charts
    };

    var chart;
       if(c=="ColumnChart") // Column Charts
        chart=new google.visualization.ColumnChart(document.getElementById('chart_div1'));
       else if(c=="PieChart") // Pie Charts
        chart=new google.visualization.PieChart(document.getElementById('piechart_div1'));
       else if(c=="BarChart") // Bar Charts
        chart=new google.visualization.BarChart(document.getElementById('bar_div1'));

       chart.draw(data, options);
   }
}
