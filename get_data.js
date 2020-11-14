const {exec} = require("child_process");
for (let i = 0; i < 300; i++) {
    let key = new Date().getTime();
    const command = `curl https://gop.captcha.garena.com/image?key=${key} --output data/${key}.jpg`;
    exec(command, (error, stdout, stderr) => {
    });
}
