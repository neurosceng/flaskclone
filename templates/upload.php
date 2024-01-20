<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>画像をアップロード</title>
</head>
<body>
    <h1>画像をアップロード</h1>


    <form method="POST" action="upimg.php" enctype="multipart/form-data">

    <input type="file" name="upimg" accept="image/*">
    <input type="submit">

    </form>

</body>
</html>
