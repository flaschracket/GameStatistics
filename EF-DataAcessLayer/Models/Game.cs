using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EF_DataAcessLayer.Models
{
    public class Game
    {
        public int GameID { get; set; }
        public string? Name { get; set; }
        public List<Player>? Players { get; set; }
        public int? CurrentRound { get; set; }
        public int? CurrentStep { get; set; }
    }
}
