import React, { useState } from 'react'
import { Link } from 'react-router-dom';
import { Bar } from 'react-chartjs-2'
import axios from 'axios'
import { BackendHost } from '../Api/BackendHost'

const MultipleHome = () => {
    const [File, setFile] = useState()
    const [BGcolor, setBGcolor] = useState("#050505")
    const [Data, setData] = useState()

    //Submit all data
    const submitFile = (e) => {
        e.preventDefault();

        var URL = `${BackendHost}/many`
        const config = { headers: { 'Content-Type': 'multipart/form-data' } }

        let formData = new FormData();
        formData.append('file', File);
        formData.append('BGcolor', BGcolor);

        axios
            .post(URL, formData, config)
            .then((res) => {
                setData(res.data);
                console.log(res.data);
            })
            .catch((err) => console.log(err));
    }

    //Uplaod file to sate
    const uploadFile = (e) => {
        setFile(e.target.files[0]);
    }

    //Download Image
    const download_img = (el) => {
        var canvas = document.getElementsByTagName("canvas")
        var ctx = canvas.getContext("2d");
        // var ox = canvas.width / 2;
        // var oy = canvas.height / 2;
        // ctx.font = "42px serif";
        // ctx.textAlign = "center";
        // ctx.textBaseline = "middle";
        // ctx.fillStyle = "#800";
        // ctx.fillRect(ox / 2, oy / 2, ox, oy);

        // var image = canvas.toDataURL("image/jpg");
        // el.href = image;
        console.log(ctx);
    }

    return (
        <div>
            <form className="file_form" method="post" encType="multipart/form-data">
                <input
                    onChange={uploadFile}
                    name="csvfile"
                    id="fileSelect" type="file"
                    accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
                />
                <input
                    type="submit"
                    name="submit"
                    value="Upload"
                    className="submit_button"
                    onClick={submitFile}
                />
                <input
                    name="color_picker"
                    type="color"
                    className="color_picker"
                />
            </form>

            <Link to='/' className="multiplechart">
                Charts with single data
            </Link>

            <div className="rest_website canv">
                {Data !== undefined ?
                    <>
                        <Bar
                            height={window.innerWidth < 400 ? 400 : null}
                            data={{
                                labels: [...Data.labels],
                                datasets: [
                                    Data.datas.map((obj, index) => {
                                        return (
                                            {
                                                label: 'Nmber Of Cases',
                                                data: [...Data.datas[index]],
                                                backgroundColor: [Data.backgroundcolor],
                                                borderWidth: 1
                                            }
                                        )
                                    })
                                ]
                            }}
                            options={{
                                scales: {
                                    y: {
                                        beginAtZero: true
                                    },
                                    responsive: true,
                                    title: {
                                        display: true,
                                        text: "Covid Data Sets"
                                    },
                                    maintainAspectRatio: true,
                                }
                            }}
                        />

                        <a id="download" download="chartimage.jpg" href="" onClick={() => download_img(this)}>
                            Download to .jpg
                        </a>
                    </> :
                    ''
                }
            </div>
        </div>
    )
}

export default MultipleHome
