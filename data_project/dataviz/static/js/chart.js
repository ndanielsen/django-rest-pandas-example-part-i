var chart = c3.generate({
    bindto: '#chart',

    data: {
        url: 'data.csv',
        type: 'bar',
        hide: ['row'],
        labels: false,
        x: 'WARD',
    },

    bar: {
        width: {
            ratio: 0.5 // this makes bar width 50% of length between ticks
        }
    },

    axis: {
        x: {
          type: 'category' // this needed to load string x value
        },
        y:{
          label: 'Total Public Artworks'
        },
    },

    legend: {
        show: false
    }
});
