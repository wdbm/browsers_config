# browsers

Note that this repository is not fully tested.

This is a browsers configuration.

# setup

```Bash
git clone https://github.com/wdbm/browsers_config.git
cd browsers_config
./setup.sh
cd ..
rm -rf browsers_config
```

# search engines, notifications and new tab

- Set the default search engine to StartPage.
- Block all requests asking to allow notifications.
- Set the new tab page to empty.

# blocking

Right click on the uBlock Origin icon, select "Options", then in the tab "My filters", add the following filters and apply the changes:

```
youtube.com/get_endscreen?
youtube.com##.subscribecard-endscreen
youtube.com##.ytp-ce-element
youtube.com##.ytp-ce-element-show
youtube.com##.ytp-pause-overlay
youtube.com##.ytp-scroll-max.ytp-scroll-min.ytp-pause-overlay
youtube.com##.ytp-title-channel
```

# privacy

## DNS over HTTPS

Access Connection Settings and select "Enable DNS over HTTPS".

# credentials storage

- [Amazon UK](https://www.amazon.co.uk/)
- [AskUbuntu](https://askubuntu.com)
- [BitBucket](https://bitbucket.org/)
- [CERN](https://login.cern.ch)
- [DeviantArt](https://www.deviantart.com/)
- [Dropbox](https://www.dropbox.com)
- [GitHub](https://www.github.com)
- [Patreon](https://www.patreon.com/)
- [PayPal](https://www.paypal.com)
- [ProtonMail](https://protonmail.com/)
- [Reddit](https://www.reddit.com)
- [Tumblr](https://www.tumblr.com/)
- [Twitter](https://www.twitter.com)

# save as MHTML (web page in single file) (Chromium)

- <chrome://flags/#save-page-as-mhtml>
- Enable and relaunch.
- Save pages as `.MHTML` files.

# extensions

|**functionality**                                     |**classes**           |**better alternative**                                                                          |**references, comments**                                                                  |**Firefox extension**                                                                                                                                                                                                           |**Chromium extension**                                                                                                                                                                                                                                                            |
|------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|StartPage search                                      |search                |                                                                                                |                                                                                          |[Startpage HTTPS Privacy Search Engine](https://addons.mozilla.org/en-US/firefox/addon/startpage-https-privacy-search)                                                                                                          |Add search engine: www.startpage.com, keyword: startpage, search engine: URL with `%s` in place of query: `https://startpage.com/do/search?q=%s`                                                                                                                                  |
|ad highlighter                                        |adblock               |                                                                                                |[**Ad-versarial: Defeating Perceptual Ad-Blocking**](https://arxiv.org/pdf/1811.03194.pdf)|                                                                                                                                                                                                                                |[Perceptual Ad Highlighter](https://chrome.google.com/webstore/detail/perceptual-ad-highlighter/mahgiflleahghaapkboihnbhdplhnchp)                                                                                                                                                 |
|adblock                                               |adblock               |                                                                                                |                                                                                          |[uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin), [AdBlock Plus](https://addons.mozilla.org/en-US/firefox/addon/adblock-plus)                                                                      |[uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origi/cjpalhdlnbpafiamejdnhcphjbkeiagm), [AdBlock](https://chrome.google.com/webstore/detail/adblock/gighmmpiobklfepjocnamgkkbiglidom)                                                                           |
|Decentraleyes                                         |security              |                                                                                                |                                                                                          |[Decentraleyes](https://addons.mozilla.org/en-US/firefox/addon/decentraleyes)                                                                                                                                                   |[Decentraleyes](https://chrome.google.com/webstore/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj)                                                                                                                                                                         |
|hide website objects                                  |security              |                                                                                                |                                                                                          |[Nuke Anything Enhanced](https://addons.mozilla.org/en-US/firefox/addon/nuke-anything-enhanced)                                                                                                                                 |                                                                                                                                                                                                                                                                                  |
|undermine tracking                                    |security              |                                                                                                |                                                                                          |[Privacy Possum](https://addons.mozilla.org/en-US/firefox/addon/privacy-possum/)                                                                                                                                                |                                                                                                                                                                                                                                                                                  |
|autodelete cookies with closed tab                    |security              |                                                                                                |                                                                                          |[Cookie AutoDelete](https://addons.mozilla.org/en-US/firefox/addon/cookie-autodelete)                                                                                                                                           |                                                                                                                                                                                                                                                                                  |
|bypass paywalls                                       |security              |                                                                                                |                                                                                          |[Bypass Paywalls](https://addons.mozilla.org/en-US/firefox/addon/bypasspaywalls)                                                                                                                                                |                                                                                                                                                                                                                                                                                  |
|GUI for control of website requests                   |security              |                                                                                                |                                                                                          |[uMatrix](https://addons.mozilla.org/en-US/firefox/addon/umatrix)                                                                                                                                                               |[uMatrix](https://chrome.google.com/webstore/detail/umatrix/ogfcmafjalglgifnmanfmnieipoejdcf)                                                                                                                                                                                     |
|Facebook fbclid remover                               |security              |                                                                                                |[fbclid-fixer](https://github.com/andreimaxim/fbclid-fixer)                               |[Facebook fbclid Fixer](https://addons.mozilla.org/en-US/firefox/addon/fbclid-fixed)                                                                                                                                            |                                                                                                                                                                                                                                                                                  |
|NewsGuard                                             |counter-disinformation|                                                                                                |[NewsGuard](https://www.newsguardtech.com)                                                |[NewsGuard](https://addons.mozilla.org/en-US/firefox/addon/newsguard)                                                                                                                                                           |[NewsGuard](https://chrome.google.com/webstore/detail/newsguard/hcgajcpgaalgpeholhdooeddllhedegi)                                                                                                                                                                                 |
|reload tabs                                           |ergonomics            |                                                                                                |                                                                                          |[Reload All Tabs](https://addons.mozilla.org/en-US/firefox/addon/reload-all-tabs)                                                                                                                                               |[Reload All Tabs](https://chrome.google.com/webstore/detail/reload-all-tabs/midkcinmplflbiflboepnahkboeonkam)                                                                                                                                                                     |
|empty new tab page                                    |ergonomics            |                                                                                                |                                                                                          |New Tab Preferences > disable top sites, highlights, snippets                                                                                                                                                                   |[Empty New Tab Page](https://chrome.google.com/webstore/detail/empty-new-tab-page/dpjamkmjmigaoobjbekmfgabipmfilij)                                                                                                                                                               |
|custom new tab page                                   |ergonomics            |                                                                                                |                                                                                          |[Speed Dial](https://addons.mozilla.org/en-US/firefox/addon/fvd-speed-dial)                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |
|dark theme for pages                                  |ergonomics            |                                                                                                |                                                                                          |[Dark Reader](https://addons.mozilla.org/en-US/firefox/addon/darkreader)                                                                                                                                                        |[DarkReader](https://chrome.google.com/webstore/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh)                                                                                                                                                                              |
|fix input elements for dark desktop environment themes|ergonomics            |                                                                                                |                                                                                          |[Text Contrast for Dark Themes](https://addons.mozilla.org/en-US/firefox/addon/text-contrast-for-dark-themes/)                                                                                                                  |                                                                                                                                                                                                                                                                                  |
|Reddit Enhancement Suite                              |ergonomics            |                                                                                                |                                                                                          |[Reddit Enhancement Suite](https://addons.mozilla.org/en-US/firefox/addon/reddit-enhancement-suite)                                                                                                                             |[Reddit Enhancement Suite](https://chrome.google.com/webstore/detail/reddit-enhancement-suite/kbmfpngjjgdllneeigpgjifpgocmfgmb)                                                                                                                                                   |
|Old Reddit Redirect                                   |ergonomics            |                                                                                                |                                                                                          |[Old Reddit Redirect](https://addons.mozilla.org/en-GB/firefox/addon/old-reddit-redirect)                                                                                                                                       |                                                                                                                                                                                                                                                                                  |
|save tabs                                             |ergonomics            |                                                                                                |                                                                                          |[Tab Session Manager](https://addons.mozilla.org/en-US/firefox/addon/tab-session-manager/), [Session Manager](https://addons.mozilla.org/en-US/firefox/addon/session-manager) (not compatible with current version of Firefox)  |[Session Buddy](https://chrome.google.com/webstore/detail/session-buddy/edacconmaakjimmfgnblocblbcdcpbko)                                                                                                                                                                         |
|enable/disable history                                |ergonomics            |                                                                                                |                                                                                          |                                                                                                                                                                                                                                |[History On/Off](https://chrome.google.com/webstore/detail/history-onoff/ljbpakpmiimdmblcjjhhbfabbkmcgmdp)                                                                                                                                                                        |
|copy multiple things                                  |ergonomics            |                                                                                                |                                                                                          |[Text MultiCopy](https://addons.mozilla.org/en-US/firefox/addon/text-multicopy/)                                                                                                                                                |                                                                                                                                                                                                                                                                                  |
|force enable right click                              |ergonomics            |                                                                                                |                                                                                          |[Absolute Enable Right Click & Copy ](https://addons.mozilla.org/en-US/firefox/addon/absolute-enable-right-click)                                                                                                               |[Enable right click](https://chrome.google.com/webstore/detail/enable-right-click/hhojmcideegachlhfgfdhailpfhgknjm)                                                                                                                                                               |
|Bandcamp download                                     |media                 |                                                                                                |                                                                                          |                                                                                                                                                                                                                                |[Bandcamp Downloader](https://chrome.google.com/webstore/detail/bandcamp-downloader/nmoobgpmablfmgchfjnhkbloaobiogeh)                                                                                                                                                             |
|images download                                       |media                 |                                                                                                |                                                                                          |[Image Picker](https://addons.mozilla.org/en-US/firefox/addon/image-picker) (not compatible with current version of Firefox), [Download all Images](https://addons.mozilla.org/en-US/firefox/addon/save-all-images-webextension)|[Image Downloader](https://chrome.google.com/webstore/detail/image-downloader/cnpniohnfphhjihaiiggeabnkjhpaldj)                                                                                                                                                                   |
|download largest image found in each tab              |media                 |                                                                                                |                                                                                          |[Tab Image Saver](https://addons.mozilla.org/en-US/firefox/addon/tab-image-saver) (preferences: tab direction: all tabs, include current tab)                                                                                   |                                                                                                                                                                                                                                                                                  |
|DeviantArt download                                   |media                 |[gallery-dl](https://github.com/mikf/gallery-dl)                                                |                                                                                          |                                                                                                                                                                                                                                |[DeviantArt downloader](https://chrome.google.com/webstore/detail/deviantart-downloader/kdcokocnkphjbaelobcehjokdleflnmj), [DeviantArt easy download](https://chrome.google.com/webstore/detail/deviantart-easy-download/fhljkabkmnoeecgibakgnkkdmheccecg)                        |
|Tumblr download                                       |media                 |[gallery-dl](https://github.com/mikf/gallery-dl), [tumblr_dl](https://github.com/wdbm/tumblr_dl)|                                                                                          |                                                                                                                                                                                                                                |[Download Tumblr raw images](https://chrome.google.com/webstore/detail/download-tumblr-raw-image/fpojonadgdgbdcliijkjibcapfbmllod)                                                                                                                                                |
|Tumblr higher resolution                              |media                 |                                                                                                |                                                                                          |[Tumblr High Quality](https://addons.mozilla.org/en-US/firefox/addon/tumblr-high-quality)                                                                                                                                       |                                                                                                                                                                                                                                                                                  |
|Twitter higher resolution, downloadable               |media                 |                                                                                                |                                                                                          |[Twitter View Original Images](https://addons.mozilla.org/en-US/firefox/addon/twitter-gensun-view)                                                                                                                              |                                                                                                                                                                                                                                                                                  |
|Facebook download                                     |media                 |                                                                                                |                                                                                          |                                                                                                                                                                                                                                |[FBDown Video Downloader](https://chrome.google.com/webstore/detail/fbdown-video-downloader/fhplmmllnpjjlncfjpbbpjadoeijkogc), [ExtensionVideo & GIF Downloader For Facebook](https://chrome.google.com/webstore/detail/video-gif-downloader-for/ajanondpapegkikdhmmhmoogcaajdokn)|
|stream media download                                 |media                 |                                                                                                |                                                                                          |[Video DownloadHelper](https://addons.mozilla.org/en-US/firefox/addon/video-downloadhelper)                                                                                                                                     |                                                                                                                                                                                                                                                                                  |
|*obsolete*: Hooktube redirect                         |media                 |                                                                                                |                                                                                          |[Hooktube Redirect](https://addons.mozilla.org/en-US/firefox/addon/hooktube-redirect)                                                                                                                                           |                                                                                                                                                                                                                                                                                  |
|capture page                                          |save                  |                                                                                                |                                                                                          |[Firefox Screenshots](https://screenshots.firefox.com), [GCLI](https://developer.mozilla.org/en-US/docs/Tools/GCLI): `Shift` `F2`, `screenshot --fullpage 2018-05-31T1725Z.png`                                                 |[Full Page Screen Capture](https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl), [Awesome Screenshot](https://chrome.google.com/webstore/detail/awesome-screenshot-screen/nlipoenfbbikpbjkfpfillcgkoblgpmj)                       |
|MetaMask                                              |crypto                |                                                                                                |                                                                                          |[MetaMask](https://addons.mozilla.org/en-US/firefox/addon/ether-metamask)                                                                                                                                                       |[MetaMask](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn)                                                                                                                                                                                   |
|web page translation                                  |language, translation |                                                                                                |                                                                                          |[Google Translator for Firefox](https://addons.mozilla.org/en-US/firefox/addon/google-translator-for-firefox)                                                                                                                   |inbuilt                                                                                                                                                                                                                                                                           |
