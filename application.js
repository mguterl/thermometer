$(function() {
  var noLabel = ''

  Highcharts.setOptions({
    chart: {
      backgroundColor: '#ddd'
    },
    credits: {
      enabled: false
    }
  });

  $('#last-48-hours-chart').highcharts({
    title: {
      text: noLabel
    },
    xAxis: {
      categories: ['2014-04-30 00:00', '2014-04-30 00:05', '2014-04-30 00:10', '2014-04-30 00:15'],
      labels: {
        enabled: false
      }
    },
    yAxis: {
      title: {
        text: noLabel
      },
      plotLines: [{
        value: 0,
        width: 1,
        color: '#808080'
      }]
    },
    tooltip: {
      valueSuffix: '°F'
    },
    series: [{
      name: 'Inside',
      color: '#555',
      data: [70, 70, 71, 69],
    }]
  });


  $('#daily-average-chart').highcharts({
    title: {
      text: noLabel
    },
    xAxis: {
      categories: ['2014-04-30 00:00', '2014-04-30 00:05', '2014-04-30 00:10', '2014-04-30 00:15'],
      labels: {
        enabled: false
      }
    },
    yAxis: {
      title: {
        text: noLabel
      },
      plotLines: [{
        value: 0,
        width: 1,
        color: '#808080'
      }]
    },
    tooltip: {
      valueSuffix: '°F'
    },
    series: [{
      name: 'Inside',
      color: '#555',
      data: [70, 70, 71, 69],
    }]
  });
});
