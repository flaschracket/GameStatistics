using GameResources.Game.Resource;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game.Resource
{
    public class Resource: IResource
    {
        public object resourceOwner;
        public Enum GetStatus()
        {
            throw new NotImplementedException();
        }

        public Enum GetVariation()
        {
            throw new NotImplementedException();
        }

        public bool IsPublic()
        {
            throw new NotImplementedException();
        }

        //?resourcetype should be out of object. each resource is one of them
        public enum ResourceVariation
        {
            Board,
            Card,
            Hardware,
            Function,
            Bazar,
        }
        public enum ResourceType
        {
            Public,
            Private,
        }
        public enum Hardware
        {
            CPU
        }
    }
}
