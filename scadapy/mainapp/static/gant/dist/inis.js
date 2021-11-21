const butshowform = document.querySelector('#showform');
const form_add_task = document.querySelector('#addtask');
const popup = document.querySelector('.popup');

butshowform.addEventListener('click', () => {
  form_add_task.classList.add('open');
  popup.classList.add('popup_open');
});





var gantt_chart = new Gantt(".gantt-target", received_data,
     {
			on_click: function (task) {
				console.log(task);
				console.log('ckiked!');
			},
			on_date_change: function(task, start, end) {
				console.log(task, start, end);
			},
			on_progress_change: function(task, progress) {
				console.log(task, progress);
			},
			on_view_change: function(mode) {
				console.log(mode);
			},

    		view_mode: 'Day',

			language: 'ru',

		});
console.log(gantt_chart);
gantt_chart.setup_tasks(gantt_chart.tasks);
gantt_chart.refresh(gantt_chart.tasks);

//function Send_json_object(url_){
//xhr = new XMLHttpRequest();
//var url = url_;
//xhr.open("GET", url);
//xhr.setRequestHeader("Content-type", "text");
////var to_send = JSON.stringify({"tasks":gantt_chart.tasks})
//xhr.send("to_sen");
//};

function Send_json_object(url_){
$.ajax({
    url: url_,
    type: 'GET',
    contentType: 'application/json; charset=utf-8',
    processData: false,
    data: JSON.stringify(gantt_chart.tasks),
})
};


today = new Date()
today=today.toISOString().split('T')[0]
var dateControl_start = document.querySelector('input[name="start"]');
var dateControl_end = document.querySelector('input[name="end"]');
dateControl_start.value = today;
dateControl_end.value = today;
console.log(today);





