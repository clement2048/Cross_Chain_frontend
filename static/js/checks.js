$(document).ready(function () {
    // 文件上传按钮点击事件
    $("#upload_file").click(function () {
        // 打开文件选择窗口
        $("#fileInput").click();
    });

    // 文件选择变化事件
    $("#fileInput").change(function () {
        // 获取选中的文件
        var file = $("#fileInput")[0].files[0];

        if (file) {
            // 创建 FormData 对象
            var formData = new FormData();
            formData.append("file", file);

            // 发送 AJAX 请求
            $.ajax({
                type: "POST",
                url: "/upload_file_path",  // 替换为实际的后端接口地址
                data: formData,
                contentType: false,
                processData: false,
                success: function (response) {
                    // 处理成功响应，response 包含后端返回的数据
                    console.log("文件上传成功", response);

                    // 在这里处理后端返回的文件内容，例如展示在页面上
                    // 示例：显示在左侧 code-container 中
                    $(".left-container.code-container").html(response.fileContent.replace(/\n/g, '<br>'));
                    // 替换按钮文本
                    $("#version_btn").text(response.versionNumber);
                },
                error: function (error) {
                    // 处理错误
                    console.log("文件上传失败", error);
                }
            });
        }
    });







});