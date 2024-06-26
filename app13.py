<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>産学連携実習マッチングアプリ</title>
    <style>
        .reportview-container {
            background: url("background.jpg") no-repeat center center fixed;
            background-size: cover;
            padding: 20px;
            color: black; /* テキスト色を黒に変更 */
            font-size: 16px; /* フォントサイズを調整 */
        }

        form {
            margin-bottom: 20px;
        }

        #map {
            width: 100%;
            height: 500px;
        }
    </style>
</head>
<body>
    <div class="reportview-container">
        <h1>産学連携実習マッチングアプリ</h1>
        <p>これは産学連携実習マッチングのテストアプリです</p>
        <h2>R&Dマネジメント研究室</h2>

        <!-- 検索フォーム -->
        <form id="searchForm">
            <label for="lunch">昼食の提供:</label><br>
            <input type="radio" id="lunchYes" name="lunch" value="あり">
            <label for="lunchYes">あり</label><br>
            <input type="radio" id="lunchNo" name="lunch" value="なし">
            <label for="lunchNo">なし</label><br><br>

            <label for="field">興味のある分野:</label><br>
            <select id="field" name="field">
                <option value="">すべて</option>
                <option value="企画">企画</option>
                <option value="開発">開発</option>
                <option value="生産">生産</option>
            </select><br><br>

            <label for="professors">担当教授:</label><br>
            <select id="professors" name="professors" multiple>
                <option value="">すべて</option>
                <option value="江面先生">江面先生</option>
                <option value="野口先生">野口先生</option>
                <option value="若木先生">若木先生</option>
                <option value="今泉先生">今泉先生</option>
                <option value="金子先生">金子先生</option>
                <option value="永澤先生">永澤先生</option>
                <option value="李先生">李先生</option>
                <option value="茨木先生">茨木先生</option>
            </select><br><br>

            <label for="interesting">実習の面白さ:</label><br>
            <select id="interesting" name="interesting">
                <option value="">すべて</option>
                <option value="1">1 - あまり面白くない</option>
                <option value="2">2 - 少し面白い</option>
                <option value="3">3 - 普通</option>
                <option value="4">4 - 面白い</option>
                <option value="5">5 - 非常に面白い</option>
            </select><br><br>

            <input type="submit" value="会社を検索">
        </form>

        <!-- 選択された会社表示 -->
        <div id="companyInfo" style="display: none;">
            <h3>該当する会社が見つかりました:</h3>
            <select id="selected_company" name="selected_company">
                <option value="" disabled selected>会社を選択してください</option>
            </select>
        </div>

        <!-- 出発地点の入力フォーム -->
        <form id="departureForm">
            <label for="departure">出発地点:</label><br>
            <input type="text" id="departure" name="departure"><br><br>
            <input type="submit" value="出発地点から距離を確認">
        </form>

        <!-- 会社データ表示 -->
        <div id="companyData" style="display: none;">
            <h3>会社データ</h3>
            <ul id="companyDataList">
                <!-- ここに会社データが表示されます -->
            </ul>
        </div>

        <!-- 出発地点からの距離とマップ表示 -->
        <div id="mapInfo" style="display: none;">
            <h3>出発地点から会社までの情報</h3>
            <p id="distanceInfo">出発地点からの距離:</p>
            <p id="routeInfo">出発地点からのルート:</p>
            <div id="map"></div>
        </div>
    </div>

    <script>
        var companyData = {
                "川﨑株式会社": {
                    "住所": "新潟県三条市下保内４０１ー１７",
                    "昼食": "あり",
                    "分野": "開発, 企画",
                    "距離": "5 km",
                    "担当教授": "江面先生",
                    "実習時間": "8:30 - 15:30",
                    "面白さ": "3" // 会社ごとの面白さ評価
                },
                "株式会社小林設計": {
                    "住所": "新潟県三条市南新保１５－７",
                    "昼食": "なし",
                    "分野": "企画",
                    "距離": "10 km",
                    "担当教授": "野口先生",
                    "実習時間": "9:00 - 16:00",
                    "面白さ": "4"
                },
                "株式会社齋鐵": {
                    "住所": "新潟県三条市井戸場８４－８",
                    "昼食": "あり",
                    "分野": "生産",
                    "距離": "15 km",
                    "担当教授": "若木先生",
                    "実習時間": "8:15 - 16:15",
                    "面白さ": "5"
                },
                "株式会社三栄製作所": {
                    "住所": "新潟県燕市小池５０７３",
                    "昼食": "なし",
                    "分野": "企画, 開発",
                    "距離": "20 km",
                    "担当教授": "今泉先生",
                    "実習時間": "8:30 - 14:30",
                    "面白さ": "2"
                },
                "株式会社内山熔接工業": {
                    "住所": "新潟県新潟市西蒲区小吉１９３０－１",
                    "昼食": "あり",
                    "分野": "生産",
                    "距離": "20 km",
                    "担当教授": "金子先生",
                    "実習時間": "9:00 - 16:00",
                    "面白さ": "4"
                },
                "株式会社大谷製作所": {
                    "住所": "新潟県燕市吉田下中野１４８３",
                    "昼食": "なし",
                    "分野": "企画, 生産",
                    "距離": "10 km",
                    "担当教授": "李先生",
                    "実習時間": "9:00 - 16:00",
                    "面白さ": "3"
                },
                "株式会社東陽理化学研究所": {
                    "住所": "新潟県西蒲原郡弥彦村大戸７６１－１",
                    "昼食": "なし",
                    "分野": "開発",
                    "距離": "15 km",
                    "担当教授": "永澤先生",
                    "実習時間": "9:00 - 17:00",
                    "面白さ": "5"
                },
                "株式会社プラスワイズ": {
                    "住所": "新潟県三条市柳川新田９９７",
                    "昼食": "あり",
                    "分野": "企画, 開発",
                    "距離": "10 km",
                    "担当教授": "永澤先生",
                    "実習時間": "9:00 - 16:00",
                    "面白さ": "4"
                },
                "株式会社スリーピークス技研": {
                    "住所": "新潟県三条市塚野目２１７１",
                    "昼食": "なし",
                    "分野": "企画, 開発, 生産",
                    "距離": "5 km",
                    "担当教授": "李先生",
                    "実習時間": "9:00 - 16:00",
                    "面白さ": "5"
                },
                "北陸工業株式会社": {
                    "住所": "新潟県三条市吉野屋甲４４５",
                    "昼食": "あり",
                    "分野": "開発, 生産",
                    "距離": "5 km",
                    "担当教授": "茨木先生",
                    "実習時間": "8:45 - 16:00",
                    "面白さ": "3"
                },
                "富士印刷株式会社": {
                    "住所": "新潟県三条市猪子場新田１１２２－１",
                    "昼食": "なし",
                    "分野": "企画, 生産",
                    "距離": "10 km",
                    "担当教授": "李先生",
                    "実習時間": "9:00 - 15:00",
                    "面白さ": "4"
                },
                "株式会社タダフサ": {
                    "住所": "新潟県三条市東本成寺２７－１６",
                    "昼食": "なし",
                    "分野": "開発, 生産",
                    "距離": "10 km",
                    "担当教授": "李先生",
                    "実習時間": "9:00 - 16:00",
                    "面白さ": "2"
                },
                "株式会社ワイヤード": {
                    "住所": "新潟県三条市北新保2丁目４－１５",
                    "昼食": "なし",
                    "分野": "開発, 生産",
                    "距離": "10 km",
                    "担当教授": "李先生",
                    "実習時間": "9:00 - 16:00",
                    "面白さ": "3"
                }
            };


        // ページが読み込まれたときの初期設定
        document.addEventListener('DOMContentLoaded', function() {
            // 会社検索フォームの処理
            var searchForm = document.getElementById('searchForm');
            searchForm.addEventListener('submit', function(event) {
                event.preventDefault(); // デフォルトの送信を無効化
                var lunchValue = document.querySelector('input[name="lunch"]:checked').value;
                var field = document.getElementById('field').value;
                var professors = Array.from(document.getElementById('professors').selectedOptions).map(option => option.value);
                var interesting = document.getElementById('interesting').value;

                // ここで条件に合致する会社を選択肢に追加する処理
                var selectedCompanyDropdown = document.getElementById('selected_company');
                selectedCompanyDropdown.innerHTML = '<option value="" disabled selected>会社を選択してください</option>';

                Object.keys(companyData).forEach(function(company) {
                    var data = companyData[company];
                    if ((lunchValue === '' || data['昼食'] === lunchValue) &&
                        (field === '' || data['分野'].includes(field)) &&
                        (professors.length === 0 || professors.some(professor => data['担当教授'].includes(professor))) &&
                        (interesting === '' || data['面白さ'] === interesting)) {
                        var option = document.createElement('option');
                        option.value = company;
                        option.textContent = company;
                        selectedCompanyDropdown.appendChild(option);
                    }
                });

                // 表示領域を表示
                var companyInfo = document.getElementById('companyInfo');
                companyInfo.style.display = 'block';
            });

            // 出発地点フォームの処理
            var departureForm = document.getElementById('departureForm');
            departureForm.addEventListener('submit', function(event) {
                event.preventDefault(); // デフォルトの送信を無効化
                var departure = document.getElementById('departure').value;
                var selectedCompany = document.getElementById('selected_company').value;

                if (selectedCompany !== '') {
                    // 会社データを表示
                    displayCompanyData(selectedCompany);
                    // Google Mapsを表示
                    displayMap(selectedCompany);
                    // 出発地点からの距離情報を表示
                    displayDistanceInfo(departure, selectedCompany);
                    // 出発地点からのルート情報を表示
                    displayRouteInfo(departure, selectedCompany);

                    // 表示領域を表示
                    var companyDataDiv = document.getElementById('companyData');
                    companyDataDiv.style.display = 'block';

                    var mapInfoDiv = document.getElementById('mapInfo');
                    mapInfoDiv.style.display = 'block';
                }
            });
        });

        // 会社のデータを表示する関数
        function displayCompanyData(company) {
            var companyDataDiv = document.getElementById('companyData');
            companyDataDiv.style.display = 'block';
            var companyDataList = document.getElementById('companyDataList');
            companyDataList.innerHTML = ''; // リセット
            var data = companyData[company];
            for (var key in data) {
                if (data.hasOwnProperty(key)) {
                    var listItem = document.createElement('li');
                    listItem.textContent = `${key}: ${data[key]}`;
                    companyDataList.appendChild(listItem);
                }
            }
        }

        // Google Mapsの地図を表示する関数
        function displayMap(company) {
            var mapInfoDiv = document.getElementById('mapInfo');
            mapInfoDiv.style.display = 'block';
            var address = companyData[company]['住所'];
            var mapsUrl = `https://www.google.com/maps/embed/v1/place?q=${encodeURIComponent(address)}&key=AIzaSyC8E0eIwP5JLXT5IWIDJiLqlhM8fh9qLOw`;
            var mapFrame = document.getElementById('map');
            mapFrame.innerHTML = `<iframe width="100%" height="500" frameborder="0" style="border:0;" src="${mapsUrl}" allowfullscreen></iframe>`;
        }

        // 出発地点からの距離情報を表示する関数
        function displayDistanceInfo(departure, company) {
            var distanceInfo = document.getElementById('distanceInfo');
            distanceInfo.textContent = `${departure} から ${company} までの距離: ${companyData[company]['距離']}`;
        }

        // 出発地点からのルート情報を表示する関数
        function displayRouteInfo(departure, company) {
            var directionsService = new google.maps.DirectionsService();
            var directionsRenderer = new google.maps.DirectionsRenderer();

            var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 7,
                center: {lat: 41.85, lng: -87.65} // 中心の初期設定（適宜変更）
            });

            directionsRenderer.setMap(map);

            var start = departure;
            var end = companyData[company]['住所'];

            var request = {
                origin: start,
                destination: end,
                travelMode: 'DRIVING'
            };

            directionsService.route(request, function(response, status) {
                if (status == 'OK') {
                    directionsRenderer.setDirections(response);
                } else {
                    window.alert('ルート検索が失敗しました: ' + status);
                }
            });
        }
    </script>
    <!-- Google Maps APIの読み込み -->
    <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC8E0eIwP5JLXT5IWIDJiLqlhM8fh9qLOw&callback=initMap"></script>
</body>
</html>
