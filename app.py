from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>InfraLearners CI/CD</title>
            <style>
                body {
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    text-align: center;
                }

                .container {
                    padding: 100px 20px;
                }

                .card {
                    max-width: 650px;
                    margin: auto;
                    padding: 50px;
                    background: rgba(255, 255, 255, 0.15);
                    border-radius: 20px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                }

                h1 {
                    font-size: 42px;
                    margin-bottom: 15px;
                }

                p {
                    font-size: 20px;
                    line-height: 1.6;
                }

                .badge {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 12px 24px;
                    background: #00c853;
                    border-radius: 30px;
                    font-weight: bold;
                }
            </style>
        </head>

        <body>
            <div class="container">
                <div class="card">
                    <h1>🚀 InfraLearners CI/CD</h1>
                    <p>Welcome to my AWS CI/CD Pipeline!</p>
                    <p>
                        GitHub → CodePipeline → CodeBuild → ECR → ECS → ALB
                    </p>
                    <div class="badge">✓ Deployment Successful</div>
                </div>
            </div>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
