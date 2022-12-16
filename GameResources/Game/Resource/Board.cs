using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game.Resource
{
    class Board: Resource
    {
        public int Id { get; set; } = 0;
        public RAM boardRAM =  new();
        public int CPU { get; set; } = 1;
        public List<IFunction> BoughtFunctions { get; set; }


    }
}
