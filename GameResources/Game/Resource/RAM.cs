using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game.Resource
{
    class RAM : Resource
    {
        public int VarA { get; set;}
        public int VarB { get; set;}
        public Boolean IsANull { get; set;} = false;
        public Boolean IsBNull { get; set;} = false;
        public Boolean IsCNull { get; set;} = false;
        public Boolean IsTotalNull { get; set;} = false;

        public int SumAllNotTotal = 0;

        public int SetSumAllNotTotal()
        {
            SumAllNotTotal = 0;
            if (!IsANull) { SumAllNotTotal += VarA; }
            if (!IsBNull) { SumAllNotTotal += VarB; }
            return SumAllNotTotal;
        }
        public int GetSumAllNotTotal()
        { return SumAllNotTotal; }

    }
}