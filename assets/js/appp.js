let host = document.querySelector("#host");
let target = document.querySelector("#target");
let workButton = document.querySelector("#work");
let outputCode = document.querySelector("#code");

function uuid() {
  return ([10000000] + -1000 + -4000 + -8000 + -100000000000).replace(
    /[018]/g,
    (repl) =>
      (
        repl ^
        (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (repl / 4)))
      ).toString(16)
  );
}

async function sendBlitly(host, target) {
  let request = await fetch(`https://apiclient.${host}/api/gen-code/get-code`, {
    headers: {
      accept: "*/*",
      "accept-language": "en-US,en;q=0.9",
      "cache-control": "max-age=0",
      "content-type": "application/json",
      rid: uuid(),
      "sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": '"Linux"',
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "cross-site",
      Referer: `https://${target}`,
      "Referrer-Policy": "strict-origin-when-cross-origin",
    },
    body: `{\"screen\":\"1920 x 1080\",\"browser_name\":\"Chrome\",\"browser_version\":\"112.0.0.0\",\"browser_major_version\":\"112\",\"is_mobile\":false,\"os_name\":\"Linux\",\"os_version\":\"-\",\"is_cookies\":true,\"href\":\"https://${target}/\",\"user_agent\":\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36\",\"hostname\":\"https://${target}\"}`,
    method: "POST",
  });
  return await request.json();
}

async function sendMneylink(host, target) {
  let request = await fetch(
    `https://mneylink.com/load_traffic?&r=https://www.google.com/&w=https://${target}/`,
    {
      headers: {
        accept: "*/*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        Referer: "https://mneylink.com/",
        //"Referrer-Policy": "strict-origin-when-cross-origin",
      },
      body: null,
      method: "GET",
    }
  );
  return await request.json();
}

async function sendLinkvip(host, target) {
  let request = await fetch(`https://${host}/graph/api?action=getCodeCamp`, {
    headers: {
      accept: "*/*",
      "accept-language": "en-US,en;q=0.9",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": '"Linux"',
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-requested-with": "XMLHttpRequest",
      "Access-Control-Allow-Origin": "*",
      Referer:
        `https://linkvip.io//traffic/iframe?w=https://${target}/&v=0`,
    },
    body: "campId=338",
    method: "POST",
  });
  return await request.json();
}

document.querySelector("#copycode").onclick = function () {
  navigator.clipboard.writeText(document.querySelector("#code").value).then(
    () => {
      console.log("Content copied to clipboard");
    },
    () => {
      console.error("Failed to copy");
    }
  );
};

document.querySelector("#work").onclick = function () {
  document.querySelector("#outputcode").value = sendBlitly();
};
function copyCode() {
  var codeInput = document.getElementById("code");
  codeInput.select();
  codeInput.setSelectionRange(0, 99999);
  document.execCommand("copy");
  alert("Mã đã được sao chép!");
}

workButton.onclick = function () {
  switch (host.value) {
    case "blitly.io":
    case "manylink.vip":
      sendBlitly(host.value, target.value).then((json) => {
        outputCode.value = json.code;
      });
      break;
    case "mneylink.com":
      sendMneylink(host.value, target.value).then((json) => {
        outputCode.value = json.data.html;
      });
      break;
    case "linkvip.io":
      sendLinkvip(host.value, target.value).then((json) => {
        console.log(json)
        outputCode.value = json.message;
      })
      break;
    default:
      alert("not implemented");
      break;
  }
};
