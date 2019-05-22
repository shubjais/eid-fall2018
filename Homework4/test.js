/*
 * Homework 4 - EID - Shubham Jaiswal 
 * node.js version: v10.11.0
 * ref: https://www.w3schools.com/js/
 * https://github.com/momenso/node-dht-sensor
 * https://nodejs.org/en/docs/guides/timers-in-node/
 * 
*/
var sensor = require('node-dht-sensor');

var count= 0;

/* Arrays for storing 10 reading samples */
var temp_list = [];
var humidity_list = [];

setInterval(Data_Input, 10000);

function Data_Input() 
{
	/* Read sensor readings */
	sensor.read(22, 4, temp_humd_print);
	
	if(count == 10)
	{
		count = 0;
		var i;
		var temp_sum = 0;
		var humidity_sum = 0;
		for (i=0;i<temp_list.length;i++){
			temp_sum = temp_sum + temp_list[i];
			humidity_sum = humidity_sum + humidity_list[i];
			}
		
		/* Calculate minimum */
		console.log('Minimum Temp: ' + (Math.min(...temp_list)).toFixed(1));
		console.log('Minimum Hum: ' + (Math.min(...humidity_list)).toFixed(1));
		
		/* Calculate maximum */
		console.log('Highest Temp: ' + (Math.max(...temp_list)).toFixed(1));
		console.log('Highest Hum: ' + (Math.max(...humidity_list)).toFixed(1));
		
		/* Calculate average */
		console.log('Average Temp: ' + (temp_sum/10).toFixed(1));
		console.log('Average Hum: ' + (humidity_sum/10).toFixed(1));
		
		console.log('-------------------------------------');
		
		/* Clear arrays */
		temp_list = [];
		humidity_list = [];
	}
}


function temp_humd_print(err, temperature, humidity)
{
	/* Check when valid readings */
	if (!err) 
	{
		/* Convert degC to degF */ 
		var tempf = (temperature * 9/5) + 32.0 ;
		count=count +1;
		
		console.log(count + ' - ' +  'Temp: ' + tempf.toFixed(1) + ' degF, ' +
			humidity.toFixed(1) + '% Hum');
		
		/* add to the array */
		temp_list.push(tempf);
		humidity_list.push(humidity);
		
	}
}
