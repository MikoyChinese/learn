import calculate_rmsd as rmsd
import numpy as np


def cal_transformation_kabsch(src_points, dst_points):
    '''
    Calculates the optimal rigid transformation from src_points to dst_points.
    (Regarding the least squares error)
    
    Args:
    ------
    src_points: array, (N, 3) matrix.
    dst_points: array, (N, 3) matrix.
    
    Returns:
    ------
    R: rotaion matrix, array.
    T: translation vector, array.
    rmsd_value: float.
    '''
    
    assert src_points.shape == dst_points.shape
    if src_points.shape[1] != 3:
        raise Exception("The input data matrix had to be transposed in order to compute transformation.")
    
    #src_points = src_points.transpose()
    #dst_points = dst_points.transpose()

    src_points_centered = src_points - rmsd.centroid(src_points)
    dst_points_centered = dst_points - rmsd.centroid(dst_points)

    R = rmsd.kabsch(src_points_centered, dst_points_centered)
    rmsd_value = rmsd.kabsch_rmsd(src_points_centered, dst_points_centered)

    T = rmsd.centroid(dst_points) - np.matmul(rmsd.centroid(src_points), R)

    return R.transpose(), T.transpose(), rmsd_value
    
    
class Transformation:
    def __init__(self, rotation_matrix, translation_vector):
        self.pose_mat = np.zeros((4,4))
        self.pose_mat[:3,:3] = rotation_matrix
        self.pose_mat[:3,3] = translation_vector.flatten()
        self.pose_mat[3,3] = 1
        
    def apply_transformation(self, points):
        """ 
        Applies the transformation to the pointcloud

        Parameters:
        -----------
        points : array
            (3, N) matrix where N is the number of points

        Returns:
        ----------
        points_transformed : array
            (3, N) transformed matrix
        """
        assert(points.shape[0] == 3)
        n = points.shape[1] 
        points_ = np.vstack((points, np.ones((1,n))))
        points_trans_ = np.matmul(self.pose_mat, points_)
        points_transformed = np.true_divide(points_trans_[:3,:], points_trans_[[-1], :])
        return points_transformed
    
def inverse(self):
    """
    Computes the inverse transformation and returns a new Transformation object

    Returns:
    -----------
    inverse: Transformation

    """
    rotation_matrix = self.pose_mat[:3,:3]
    translation_vector = self.pose_mat[:3,3]

    rot = np.transpose(rotation_matrix)
    trans = - np.matmul(np.transpose(rotation_matrix), translation_vector)
    return Transformation(rot, trans)
