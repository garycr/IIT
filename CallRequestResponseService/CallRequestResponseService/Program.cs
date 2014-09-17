// This code requires the Nuget package Microsoft.AspNet.WebApi.Client to be installed.
// Instructions for doing this in Visual Studio:
// Tools -> Nuget Package Manager -> Package Manager Console
// Install-Package Microsoft.AspNet.WebApi.Client

using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Net.Http.Formatting;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace CallRequestResponseService
{
    public class ScoreData
    {
        public Dictionary<string, string> FeatureVector { get; set; }
        public Dictionary<string, string> GlobalParameters { get; set; }
    }

    public class ScoreRequest
    {
        public string Id { get; set; }
        public ScoreData Instance { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            InvokeRequestResponseService().Wait();
        }

        static async Task InvokeRequestResponseService()
        {
            using (var client = new HttpClient())
            {
                ScoreData scoreData = new ScoreData()
                {
                    FeatureVector = new Dictionary<string, string>() 
                    {
                        { "State", "0" },
                        { "Account_Length", "0" },
                        { "Int_l_Plan", "0" },
                        { "VMail_Plan", "0" },
                        { "VMail_Message", "0" },
                        { "Day_Mins", "0" },
                        { "Day_Calls", "0" },
                        { "Eve_Mins", "0" },
                        { "Eve_Calls", "0" },
                        { "Night_Mins", "0" },
                        { "Night_Calls", "0" },
                        { "Intl_Mins", "0" },
                        { "Intl_Calls", "0" },
                        { "CustServ_Calls", "0" },
                        { "Churn_", "0" },
                    },
                    GlobalParameters = new Dictionary<string, string>()
                    {
                    }
                };

                ScoreRequest scoreRequest = new ScoreRequest()
                {
                    Id = "score00001",
                    Instance = scoreData
                };

                const string apiKey = @"/fqyfFdY1wryxBTaGMfqNFNGq0z4dVvmAHnSMXq3xFnF01Dh37r/tNDO93MQ9RvNliin4TNl/NeTvJivIyBlhA=="; 
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);

                client.BaseAddress = new Uri("https://ussouthcentral.services.azureml.net/workspaces/bc6795225e2d4bcf8d414b960baad85c/services/28d6553f988b40fa8567845a0c06b4b5/score");
                HttpResponseMessage response = await client.PostAsJsonAsync("", scoreRequest);
                if (response.IsSuccessStatusCode)
                {
                    string result = await response.Content.ReadAsStringAsync();
                    Console.WriteLine("Result: {0}", result);
                }
                else
                {
                    Console.WriteLine("Failed with status code: {0}", response.StatusCode);
                }
            }
        }
    }
}

