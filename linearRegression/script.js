window.onload = function () {

    const points = [];
    $("#graph").click((e) => {
        const g = document.getElementById("graph")
        var ctx = g.getContext("2d");
        ctx.clearRect(0,0,800,400)
        points.push([e.clientX-10,410 - e.clientY])
        plot_points(points)

        let xmean = 0, ymean = 0;
        points.forEach((point) => {
            xmean += point[0];
            ymean += point[1];
        })

        xmean /= points.length
        ymean /= points.length

        let yi= 0, xi = 0;
        points.forEach((point) => {
             yi += (point[0] - xmean)*(point[1] - ymean)
             xi += (point[0] - xmean)*(point[0] - xmean)
        })

        let m = yi/xi, con = ymean - m*xmean, x_int = 10-con/m, y_int = 410-con;

        var c = document.getElementById("graph");
        var ctx = c.getContext("2d");
        if (m < 0 ) {
            ctx.beginPath();
            ctx.moveTo(0, y_int);
            ctx.lineTo(x_int, 410);
            ctx.stroke();
        }   else {
            if(con > 0 ) {
                ctx.beginPath();
                ctx.moveTo(0, 410-con);
                ctx.lineTo((400-con)/m-10, 0);
                ctx.stroke();
            }   else {
                ctx.beginPath();
                ctx.moveTo(x_int, 410);
                ctx.lineTo(800, 410-800*m-con);
                ctx.stroke();
            }
        }
    })

    function plot_points(p) {
        p.forEach((point) => {
            var c = document.getElementById("graph");
            var ctx = c.getContext("2d");
            ctx.beginPath();
            ctx.arc(point[0] + 10, 410 - point[1], 3, 0, 2 * Math.PI);
            ctx.stroke();
        })
    }



}