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
        }
    </style>
</head>

<body>
    <div class="reportview-container">
        <h1>産学連携実習マッチングアプリ</h1>
        <p>これは産学連携実習マッチングのテストアプリです</p>
        <h2>R＆Dマネジメント研究室</h2>

        <!-- Streamlitコンポーネント -->
        <form id="searchForm" method="get">
            <label for="lunch">昼食の提供:</label><br>
            <input type="radio" id="lunchYes" name="lunch" value="あり">
            <label for="lunchYes">あり</label><br>
            <input type="radio" id="lunchNo" name="lunch" value="なし">
            <label for="lunchNo">なし</label><br><br>

            <label for="field">興味のある分野:</label><br>
            <select id="field" name="field">
                <option value="企画">企画</option>
                <option value="開発">開発</option>
                <option value="生産">生産</option>
            </select><br><br>

            <label for="max_distance">大学からの最大距離(km):</label><br>
            <input type="range" id="max_distance" name="max_distance" min="0" max="20" value="20">
            <br><br>

            <label for="professors">担当教授:</label><br>
            <select id="professors" name="professors" multiple>
                <option value="江面先生">江面先生</option>
                <option value="野口先生">野口先生</option>
                <option value="若木先生">若木先生</option>
                <option value="今泉先生">今泉先生</option>
                <option value="金子先生">金子先生</option>
                <option value="永澤先生">永澤先生</option>
                <option value="李先生">李先生</option>
                <option value="茨木先生">茨木先生</option>
            </select><br><br>

            <label for="start_time">実習開始時間:</label><br>
            <input type="time" id="start_time" name="start_time" value="08:00"><br><br>

            <label for="end_time">実習終了時間:</label><br>
            <input type="time" id="end_time" name="end_time" value="15:00"><br><br>

            <!-- 新しい選択肢として実習の面白さを追加 -->
            <label for="interesting">実習の面白さ:</label><br>
            <select id="interesting" name="interesting">
                <option value="1">1 - あまり面白くない</option>
                <option value="2">2 - 少し面白い</option>
                <option value="3">3 - 普通</option>
                <option value="4">4 - 面白い</option>
                <option value="5">5 - 非常に面白い</option>
            </select><br><br>

            <input type="submit" value="Submit">
        </form>

        <!-- Streamlitからの出力 -->
        <div>
            <p>該当する会社が見つかりました:</p>
            <select id="selected_company" name="selected_company">
                <option value="川﨑株式会社">川﨑株式会社</option>
                <option value="株式会社小林設計">株式会社小林設計</option>
                <option value="株式会社齋鐵">株式会社齋鐵</option>
                <option value="株式会社三栄製作所">株式会社三栄製作所</option>
                <option value="株式会社内山熔接工業">株式会社内山熔接工業</option>
                <option value="株式会社大谷製作所">株式会社大谷製作所</option>
                <option value="株式会社東陽理化学研究所">株式会社東陽理化学研究所</option>
                <option value="株式会社プラスワイズ">株式会社プラスワイズ</option>
                <option value="株式会社スリーピークス技研">株式会社スリーピークス技研</option>
                <option value="北陸工業株式会社">北陸工業株式会社</option>
                <option value="富士印刷株式会社">富士印刷株式会社</option>
                <option value="株式会社タダフサ">株式会社タダフサ</option>
                <option value="株式会社ワイヤード">株式会社ワイヤード</option>
            </select>
        </div>

        <!-- 出発地点の入力 -->
        <form id="departureForm" method="get">
            <label for="departure">出発地点:</label><br>
            <input type="text" id="departure" name="departure"><br><br>
            <input type="submit" value="Submit">
        </form>

        <!-- 会社データ -->
        <div>
            <h3>会社データ</h3>
            <ul id="companyDataList">
                <!-- ここに会社データが表示されます -->
            </ul>
        </div>

        <!-- 会社までの距離とマップの表示 -->
        <div>
            <h3>出発地点から会社までの情報</h3>
            <p id="distanceInfo">出発地点から会社までの距離:</p>
            <p id="routeInfo">ルートの表示:</p>
            <iframe id="mapFrame" width="700" height="500" frameborder="0" style="border:0" allowfullscreen></iframe>
        </div>
    </div>

    <script>
        document.getElementById("searchForm").addEventListener("submit", function (event) {
            event.preventDefault();
            var formData = new FormData(this);
            var lunch = formData.get("lunch");
            var field = formData.get("field");
            var maxDistance = formData.get("max_distance");
            var professors = formData.getAll("professors");
            var startTime = formData.get("start_time");
            var endTime = formData.get("end_time");
            var interesting = formData.get("interesting"); // 追加された実習の面白さ

            // 選択された会社の情報を表示するための処理
            var selectedCompany = document.getElementById("selected_company").value;
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
            var selectedCompanyData = companyData[selectedCompany];
            var companyInfoHTML = "<li><h4>" + selectedCompany + "</h4><ul>";
            for (var key in selectedCompanyData) {
                if (selectedCompanyData.hasOwnProperty(key)) {
                    companyInfoHTML += "<li>" + key + ": " + selectedCompanyData[key] + "</li>";
                }
            }
            companyInfoHTML += "</ul></li>";
            document.querySelector(".reportview-container div > ul").innerHTML = companyInfoHTML;
        });

        document.getElementById("departureForm").addEventListener("submit", function (event) {
            event.preventDefault();
            var departure = document.getElementById("departure").value;
            var selectedCompany = document.getElementById("selected_company").value;
            var companyData = {
                "川﨑株式会社": "新潟県三条市下保内４０１ー１７",
                "株式会社小林設計": "新潟県三条市南新保１５－７",
                "株式会社齋鐵": "新潟県三条市井戸場８４－８",
                "株式会社三栄製作所": "新潟県燕市小池５０７３",
                "株式会社内山熔接工業": "新潟県新潟市西蒲区小吉１９３０－１",
                "株式会社大谷製作所": "新潟県燕市吉田下中野１４８３",
                "株式会社東陽理化学研究所": "新潟県西蒲原郡弥彦村大戸７６１－１",
                "株式会社プラスワイズ": "新潟県三条市柳川新田９９７",
                "株式会社スリーピークス技研": "新潟県三条市塚野目２１７１",
                "北陸工業株式会社": "新潟県三条市吉野屋甲４４５",
                "富士印刷株式会社": "新潟県三条市猪子場新田１１２２－１",
                "株式会社タダフサ": "新潟県三条市東本成寺２７－１６",
                "株式会社ワイヤード": "新潟県三条市北新保2丁目４－１５"
            };
            var companyAddress = companyData[selectedCompany];
            var distanceInfoHTML = "<p>出発地点から" + selectedCompany + "までの距離:</p>";
            var routeInfoHTML = "<p>ルートの表示:</p><iframe width=\"700\" height=\"500\" frameborder=\"0\" style=\"border:0\" allowfullscreen src=\"https://www.google.com/maps/embed/v1/directions?key=AIzaSyC8E0eIwP5JLXT5IWIDJiLqlhM8fh9qLOw&origin=" + departure + "&destination=" + companyAddress + "&mode=driving\"></iframe>";
            document.getElementById("distanceInfo").innerHTML = distanceInfoHTML;
            document.getElementById("routeInfo").innerHTML = routeInfoHTML;
        });
    </script>
</body>

</html>
