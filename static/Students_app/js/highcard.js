// Create the chart
Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Semester Wise SGPA'
    },
    // subtitle: {
    //     text: 'Click the columns to view versions. Source: <a href="http://statcounter.com" target="_blank">statcounter.com</a>'
    // },
    accessibility: {
        announceNewData: {
            enabled: true
        }
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        title: {
            text: 'Total percent market share'
        }

    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y}'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{data.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span><br>SGPA: <b>{point.y:.2f}</b><br/>'
    },

    series: [
        {
            name: "Browsers",
            colorByPoint: true,
            data: [
                {
                    name: "Summer, 2018",
                    y: 3.95,
                    drilldown: "Chrome"
                },
                {
                    name: "Fall, 2018",
                    y: 4,
                    drilldown: "Chrome"
                },
                {
                    name: "Spring, 2019",
                    y: 4,

                },

            ]
        }
    ],

});





// for payment sceame
Highcharts.chart('container1', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Payment Scheme'
    },
    subtitle: {
        text: 'XYZ International University'
    },
    accessibility: {
        announceNewData: {
            enabled: true
        }
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        title: {
            text: 'Total percent market share'
        }

    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.2f}'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:15px">{data.name}<br></span>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span><br> Payment Scheme: <b>{point.y:.2f}</b><br/>'
    },

    series: [
        {
            name: "Browsers",
            colorByPoint: true,
            data: [
                {
                    name: "Admission Fee",
                    y: 15000,
                    drilldown: "Admission Fee"
                },
                {
                    name: "Campus development Fee",
                    y: 4500,
                    drilldown: "Campus development Fee"
                },
                {
                    name: "Extra Curriculam Fee",
                    y: 750,
                    drilldown: "Extra Curriculam Fee"
                },
                {
                    name: "Lab Fee",
                    y: 2000,
                    drilldown: "Lab Fee"
                },
                {
                    name: "Rover Scout & BNCC Fee",
                    y: 1000,
                    drilldown: "Rover Scout & BNCC Fee"
                },
                {
                    name: "Semester Fee",
                    y: 15000,
                    drilldown: "Semester Fee"
                },
                {
                    name: "Tutuion Fee",
                    y: 2500,
                    drilldown: 'Tutuion Fee'
                },
                {
                    name: "smart Card",
                    y: 1000,
                    drilldown: 'smart Card'
                },
                {
                    name: "smart Card1",
                    y: 2500,
                    drilldown: 'smart Card'
                },
                {
                    name: "smart Card2",
                    y: 1500,
                    drilldown: 'smart Card'
                },
                {
                    name: "smart Cardz",
                    y: 3000,
                    drilldown: 'smart Card3'
                }
            ]
        }
    ],

});