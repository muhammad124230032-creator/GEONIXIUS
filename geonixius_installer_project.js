{
  "name": "geonixius",
  "productName": "GEONIXIUS",
  "version": "1.0.0",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "dist": "electron-builder"
  },
  "devDependencies": {
    "electron": "^30.0.0",
    "electron-builder": "^24.0.0"
  },
  "build": {
    "appId": "com.geonixius.desktop",
    "productName": "GEONIXIUS",
    "win": {
      "target": "nsis",
      "icon": "icon.ico"
    },
    "nsis": {
      "oneClick": false,
      "allowToChangeInstallationDirectory": true,
      "installerIcon": "icon.ico",
      "uninstallerIcon": "icon.ico",
      "shortcutName": "GEONIXIUS"
    }
  }
}