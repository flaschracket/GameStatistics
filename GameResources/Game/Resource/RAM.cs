using System;

namespace GameResources.Game.Resource
{
    public class RAM 
    {
        public int VarA { get; set;}
        public int VarB { get; set;}
        public Boolean IsANull { get; set;} = false;
        public Boolean IsBNull { get; set;} = false;
        //public Boolean IsCNull { get; set;} = false;
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

        public bool IsPublic()
        {
            throw new NotImplementedException();
        }

        public Enum GetStatus()
        {
            throw new NotImplementedException();
        }

        public Enum GetVariation()
        {
            throw new NotImplementedException();
        }
    }
}