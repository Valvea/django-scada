const butshowform = document.querySelector('#showform');
const deltask = document.querySelector('#deltask');
const form_add_task = document.querySelector('#addtask');
const butchangetask = document.querySelector('#changetask');
const popup = document.querySelector('.popup');
const form = document.querySelector("form");

butshowform.addEventListener('click', () => {
  form_add_task.classList.add('open');
  popup.classList.add('popup_open');
});

butchangetask.addEventListener('click', () => {
 Send_json_object({"tasks":tasks_changed,
 'task':'change'})
});


var last_cliked_task;
var tasks_changed ={'data_change':{},
                    'progress_changed':{}};




form.addEventListener("submit", function(event) {
    var els=form.elements;
    var deps=[];
    $.each(els.dependencies.selectedOptions, function(i,op) {
    deps.push(op.index);
    });

    if (gantt_chart==undefined) {
      var task = {
        id:0,
        name: els.name.value,
        start: els.start.value,
        end: els.end.value,
        progress: Number(els.progress.value),
        dependencies: '',
        custom_class: 'bar-milestone' }
      
    } else {
      deps=deps.map(it=>"Task "+String(it));
      const reducer = (previousValue, currentValue) => previousValue +","+ currentValue;
      console.log(gantt_chart.tasks.length)
      var task = {
      id: gantt_chart.tasks.length,
      name: els.name.value,
      start: els.start.value,
      end: els.end.value,
      progress: Number(els.progress.value)>0? Number(els.progress.value):1,
      dependencies: deps.length>0?deps.reduce(reducer):'',
      custom_class: 'bar-milestone' }
    }
    Send_json_object({"tasks":task,
              'task':'add'});
  });

  deltask.addEventListener("click",function(event){
    if (last_cliked_task!=undefined)
    {
      Send_json_object({"tasks":last_cliked_task,
      'task':'del'});
      gantt_chart.tasks.pop(last_cliked_task);
      gantt_chart.refresh(gantt_chart.tasks);
    }

  });


  var gantt_chart = new Gantt(".gantt-target", received_data,
  {
   on_click: function (task) {
     
     last_cliked_task=task.id;

   },
   on_date_change: function(task, start, end) {
     console.log(task, start, end);
     tasks_changed['data_change'][Number(task['id'].slice(-1))]={'start':start,'end':end}
     // tasks_changed.push({
     // 'data_change':{'id':Number(task['id'].slice(-1)) ,'start':start,'end':end}});
   },
   on_progress_change: function(task, progress) {
     console.log(task, progress);
     tasks_changed['progress_changed'][Number(task['id'].slice(-1))]={'progress':progress}
     // tasks_changed.push({'progress_changed':
     // {'id':Number(task['id'].slice(-1)),'progress':progress}});
   },
   on_view_change: function(mode) {
     console.log(mode);
   },

     view_mode: 'Day',

   language: 'ru',

 });





$('#dependencies').empty();
$.each(gantt_chart.tasks, function(_index, task) {
     $('#dependencies').append($('<option></option>').val(task.name).html(task.name));
});





// $(window).ready(function()
// {
//     $(window).bind("beforeunload", function() {
//         if (window.location.pathname=='/gant/')
//             {Send_json_object({"tasks":gantt_chart.tasks,
//           'task':'save'});
//         }
//     });
// });


today = new Date()
today=today.toISOString().split('T')[0]
var dateControl_start = document.querySelector('input[name="start"]');
var dateControl_end = document.querySelector('input[name="end"]');
dateControl_start.value = today;
dateControl_end.value = today;
console.log(today);




