function click() {
  alert("Hello World");
}

const ctx = document.getElementById("myChart").getContext("2d");

const chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "My Dataset",
        data: [10, 20, 30, 40, 50, 60, 70],
        borderColor: "blue",
        fill: false,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  },
});

chart.update();
