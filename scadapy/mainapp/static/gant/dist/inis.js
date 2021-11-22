const butshowform = document.querySelector('#showform');
const form_add_task = document.querySelector('#addtask');
const popup = document.querySelector('.popup');

butshowform.addEventListener('click', () => {
  form_add_task.classList.add('open');
  popup.classList.add('popup_open');
});


var last_cliked_task;


var form = document.querySelector("form");
form.addEventListener("submit", function(event) {
    var els=form.elements;
    var deps=[];
    $.each(els.dependencies.selectedOptions, function(i,op) {
    deps.push(op.index);
    });
    var task = {
    id: "Task "+gantt_chart.tasks[gantt_chart.tasks.length-1]._index,
    name: els.name.value,
    start: els.start.value,
    end: els.end.value,
    progress: els.progress.value,
    dependencies: deps.map(it=>"Task "+String(it)),
    custom_class: 'bar-milestone' }
    gantt_chart.tasks.push(task);
  });


var gantt_chart = new Gantt(".gantt-target", received_data,
     {
			on_click: function (task) {
				last_cliked_task=task.id;

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
gantt_chart.setup_tasks(gantt_chart.tasks);
gantt_chart.refresh(gantt_chart.tasks);

$('#dependencies').empty();
$.each(gantt_chart.tasks, function(_index, task) {
     $('#dependencies').append($('<option></option>').val(task.name).html(task.name));
});


function Send_json_object(url_){
$.ajax({
    url: url_,
    type: 'GET',
    contentType: 'application/json; charset=utf-8',
    processData: false,
    data: JSON.stringify(gantt_chart.tasks)
})
};

$(window).ready(function()
{
    $(window).bind("beforeunload", function() {
        if (window.location.pathname=='/gant/')
        {Send_json_object('/get_json');}
    });
});


today = new Date()
today=today.toISOString().split('T')[0]
var dateControl_start = document.querySelector('input[name="start"]');
var dateControl_end = document.querySelector('input[name="end"]');
dateControl_start.value = today;
dateControl_end.value = today;
console.log(today);




