##全平台DUO passcode开源获取程序 python ver

听说anyconnect也要MFA了那就先写个自动获取passcode的组件x

和移动端DUO push说再见）

简单说明（过两天写详细说明）
首次使用:
1. pip install pyotp （或者cd进本文件所在的文件夹然后pip install -r requirements.txt）
2. 在start.nyu.edu注册一个新的android平板设备,在扫描QR code那一步右键二维码选择复制图片链接，
3. 然后在secret.conf里把链接粘贴进去（注意保留引号）
4. 然后运行init.py


之后每次想要passcode的话运行passcode.py就会弹出来一个passcode啦