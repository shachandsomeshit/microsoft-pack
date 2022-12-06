import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://account.microsoft.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
}

params = {
    'partner': 'amc',
    'market': 'en-us',
    'uhf': '1',
}

response = requests.get('https://mem.gfx.ms/meversion', params=params, headers=headers)
print(response.cookies)

import requests

cookies = {
    'AMCSecAuth': 'FAB6BxRUIIj416n9XIo%2BZGOl8TgTAndtFwNmAAAEgAAACPsqdtzqkL1tOAfzIAuj%2BoLukLK6iBjeefgCAaV/Wy01WT5pNQGn8x5uy5imhcadd6%2BxM5SWRGZ0iXH%2BkgRyZmBMMzxOz8tARdWw/sLKypV8MRAi97KXhKsiwiKEKJGJTN5pMzZUvwCAcfiAkX9VRXl6mseGgCk1Y9/r%2BoAy%2BLScq7SdXRPBKAfel/pDJjMWiZA0M0et4FK/Po/deiovHqSAN9u2fVtGIED5bEtETEi2bX6VT7oK8AyEkp9xoyN4JANzvGRL1RNeN5HVOrmh9rMZpnVUEqV8oLgcrwdwGMBgkaBEsFZJv4GdikS63RZ/Rfvg6PdF/eIaAJy7Ezi/819/udNvHDk8amyXbLBhM8dfBt1Gv9Kf53o1Faht0TH5q/7W4CoGfdQUi1dMWN9iz9iGaVToG/vtuIppu/dUNP%2BT4QCOEUlMO3A8rRk%2Bqde/nnh/znOjpmWrsAciG%2B3ZESZKuzzmtTKGwC6qCouf%2BCC3N74lMldX5lLV/z60g%2BJqNu1%2Btxde7YLie/0LCkZ0q5oN1Hvpp0HB3zOGfP3yWURhZLtRCheaFtjankhjHtNM5H0wzbPnUAqyzB3BrtAPS5Sb4i6jqnJONOMFc11Iv6c4c6ANfzeLGz6wc46TOm5iphQbXYnJA9duNl3484QlYdkXnRAj9zWdEx/PMs/QvQVTsPccyaM5NZHlUsU/9cGvudb4OL3Gj6CbpXFEEVaYw%2BHEsj2Yc6is2IJAMQuFj%2BmiHcRwt1t63xPClpkwkxV7KqBZLmpp06L/l6qYJQ2B6rno147RXgX%2BY%2B5Lp/vu%2BICXIsQjmV4TuF1kNgX16opgsgqrjgG83/MgPtOt8/rupQss3dA6W7ieLuHp%2BxqrImKBR6qAAHl8gFVGt%2B%2Baxu0MAw2wE0FKY7qmiJmyqX8ELToEAQfSbLeeU2p14SObKOv8fLshdW4rJj3BhS1QUKgqnG1EE2n/BQT%2B7kleIVip4ZCYAeIZaszjVt%2B4w5egbkfMFZkmINNLGK6MFVQDMqp4p6vM0HgPfTixt2kRbctGVIZBTEg8W%2BRUv8Ve5mnGhKWrVTdt4F81sDyH1rOg4U%2BCjJud68n50KYtH4v7OoU63Pzqxl7xG6LB2x/BdY%2BZLwxBzxE4RUyB0C2Ql%2BXOztpb98ZyLVMu/ubuJRBQXLzlD4HEhP7PKndmP6mRRgPe7z8JrtI589BhYjJ9k6qfwEKhGv/42tMnGo2C8zOjVb15vyfjM8Nor%2BA2ZtI9fAbLvbwLfZV8Ww5cX0gX7VsKUT40PT34%2B/HoE2/KuTslebGwghlI3r6MIwgZIfTw7rj/hHdSpNyUqVfzZzrv4d4xi19TjB5d8KFCFjA2WMu1BJhw45T1VLtX5KuBxH8O%2Bz7yw%2BOZ/N0MDQ/SmoNWY/0x2NFy5%2Bbz2stEEisROeQhf4MHxlbBFpdg9hck8x0VJ%2B7a8Yty0nM9ZC8/6rHeZCjWojLKIbrqrr7O87MXpqz5azI022CAJsfrxzBU6NLYi48if5ZeyJyWLqqc5whyrBzCX4n3tTRYROci8G0oeCOAx7IzhPKd2N6H7ULPW/a6ssCASszYd8yfza4x6sAROyAoDrozEmxDmeUUtOSZ2CcjqD2mTHXCezSal0vT2TDwHEWEw5pARLNVionljLu2UHs3gkgJlkp2c3WrdMHylxy3Qu8qrdQc4x8oFA0sNxt9p3M4Js6h148SZ9OareVfYjVT01Sv7zALS7lt81m6J2XeJFsISy9M8H7bqhnkyzP8y%2Bw7P94IKGvWKbsBM4TLb4hfGlO7hqTWxi7Shg92vxbMCOphGFLEJYqqYogKztOcHy0iGIg6Tyak/kPopW/BnhFUnOs9n5bR2tZ1F0Nk0dFFdhq7ymWuho6XsfMl6qjatB54jsLGfoDr/IE15F6mwyKxsdzNqbTFBA%2BVSoNRIhVdXVWjR3BwNGQ7m7BMiV67eAY3a4dPUZqym1mWLCDTyq2GjO032bYmFAKGO68c%2BrTnEhVl3SuF8rsSbluw3neLddkpuZ3oJQ9qKhzflSdUMUBA36Y6%2Bs%2BsTStR96t6GPA3s/yBdMosUnWo5Ranjo5n1TdSv9qJJT7ZbQl5sLrPWU7u84wrchQlE/uRg7u/t7TzvX444dmaXAlzrAvHcmXaVjo7k5chXWdELjvYBEU1SG%2B5PVeI0uNWj1WfRuW7arHS/R4abp0Uzce6/7%2BAioJQqdUSDjgU%2BaROvxmkUBcEnIZW73MjzB6L39myWHLN3Fa2fFdfAEqmayTUdOD4ngcevd9sbC3oavZMmOePdD1SatJtK9qLk2eIUiEFGZkuEzFyFR8seU9NnFa%2BjF7U%2BSIQOdUNUosmaSrfs%2Buy1w1/rp3tfs9nZIWoMMmsZPxNigPgp0bIWYJmXbDGkKLAWFANJPrKKA3Yeoeh3mi64U26D9I/krng6BiM6YP7uTTsmCXcTtr09mfhP9vnVMWy2LzooKVUewjoB4YUACZdAhMFvsAzIX0uTpAQ%2BOaSDs6s',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://account.microsoft.com/?lang=en-US&refd=account.live.com&refp=landing&mkt=EN-US',
    'X-TzOffset': '120',
    'X-IsCloudOS': 'false',
    'X-Requested-With': 'XMLHttpRequest',
    'Correlation-Context': 'v=1,ms.b.tel.market=en-US',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'excludeWindowsStoreInstallOptions': 'false',
    'excludeLegacySubscriptions': 'true',
    'isReact': 'true',
    'includeCmsData': 'false',
}

response = requests.get('https://account.microsoft.com/services/api/subscriptions', params=params, cookies=cookies, headers=headers)
print(response.text)